from sqlalchemy import create_engine, text,Column, Integer, String,Text, TIMESTAMP, ForeignKey, Numeric, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, relationship
import pandas as pd
import matplotlib.pyplot as plt

#connexion a la base ...username:mdp@serveur/nom de la base
engine = create_engine('postgresql://postgres:Test_conn@localhost/numcity')

# creer une classe (base) parent pour que les classes vont heriter pour devenir des tables ORM
Base = declarative_base()



class Citoyen(Base):
    __tablename__ = 'citoyen'
    user_id = Column(String(50), primary_key=True)
    user_email = Column(String(50), nullable=False)
    user_mdp = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    #relationship between citoyen et tous ces demandes(one to many)
    demandes = relationship("Demande", back_populates="citoyen")


class Categorie(Base):
    __tablename__ = 'categorie'
    categorie_id = Column(String(50), primary_key=True)
    categorie_nom = Column(String(50), nullable=False)
    #relation entre categorie et tous les lieux
    lieux = relationship("Lieu", back_populates="categorie")


class Zone(Base):
    __tablename__ = 'zone'
    zone_id = Column(String(50), primary_key=True)
    zone_nom = Column(String(50), nullable=False)
    #relation entre zone et tous les lieux
    lieux = relationship("Lieu", back_populates="zone")


class Lieu(Base):
    __tablename__ = 'lieu'
    lieu_id = Column(String(50), primary_key=True)
    lieu_latitude = Column(Numeric(9,6), nullable=False)
    lieu_longtitude = Column(Numeric(9,6), nullable=False)
    #foreign keys always on the many side
    zone_id = Column(String(50), ForeignKey('zone.zone_id'), nullable=False)
    categorie_id = Column(String(50), ForeignKey('categorie.categorie_id'), nullable=False)

    zone = relationship("Zone", back_populates="lieux")
    categorie = relationship("Categorie", back_populates="lieux")
    demandes = relationship("Demande", back_populates="lieu")


class Demande(Base):
    __tablename__ = 'demande'
    demande_id = Column(String(50), primary_key=True)
    demande_type = Column(String(20), nullable=False)
    demande_description = Column(Text)
    demande_date = Column(TIMESTAMP, nullable=False)
    lieu_id = Column(String(50), ForeignKey('lieu.lieu_id'), nullable=False)
    user_id = Column(String(50), ForeignKey('citoyen.user_id'), nullable=False)

    lieu = relationship("Lieu", back_populates="demandes")
    citoyen = relationship("Citoyen", back_populates="demandes")


# creation d'une session pour interoger la base
Session = sessionmaker(bind=engine)
session = Session()

# requete : recuperer toutes les demandes de type Modification
for d in session.query(Demande).filter_by(demande_type='Modification'):
    print(d.demande_id, d.demande_description)

#all categories
res = session.query(Categorie).all()
for r in res:
    print(r.categorie_id)
#jointures : chaque demande avec le lieu et le citoyen qui a fait cette demande
# jointure sans relationship
req = (session.query(
    Demande.demande_id,
                    Demande.demande_type,
                    Demande.demande_description,
                    Demande.demande_date,
                    Citoyen.user_name.label('citoyen'),
                    Citoyen.user_email,
                    Lieu.lieu_id,
                    Lieu.lieu_latitude,
                    Lieu.lieu_longtitude
                    )
                    .join(Citoyen, Demande.user_id == Citoyen.user_id)
                    .join(Lieu, Demande.lieu_id == Lieu.lieu_id)
                    .order_by(Demande.demande_date.desc())
                    .all()
)

#jointure avec relationship
req = (
    session.query(
        Demande.demande_id,
        Demande.demande_type,
        Demande.demande_description,
        Demande.demande_date,
        Citoyen.user_name.label('citoyen'),
        Citoyen.user_email,
        Lieu.lieu_id,
        Lieu.lieu_latitude,
        Lieu.lieu_longtitude
    )
    .join(Demande.citoyen) #join(Citoyen, Demande.user_id == Citoyen.user_id)
    .join(Demande.lieu)
    .order_by(Demande.demande_date.desc())
    .all()
)


df = pd.DataFrame(req)
print(df)

# agregation count()

results = session.query(Demande.demande_type,func.count(Demande.demande_type)).group_by(Demande.demande_type).all()
print(results)

 # like les noms qui ont ali 

res2 = session.query(Citoyen.user_name).filter(Citoyen.user_name.like("%ali%")).all()
print(res2)

# nb demandes par categorie de lieu

stmt = session.query(Categorie.categorie_nom, func.count(Demande.demande_id).label('nb_demandes')).join(Lieu, Demande.lieu_id == Lieu.lieu_id).join(Categorie, Categorie.categorie_id == Lieu.categorie_id).group_by(Categorie.categorie_id).order_by(func.count(Demande.demande_id).desc()).all()
df2 = pd.DataFrame(stmt)
print(df2)

plt.figure(figsize=(6,4))
plt.bar(df2['categorie_nom'], df2['nb_demandes'])
plt.title("Nombre de demandes par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Nombre de demandes")
plt.show()

# nb demandes par zone
stmt2 = session.query(Zone.zone_nom, 
                    func.count(Demande.demande_id).label('nb_demandes')
                    ).join(Lieu, Demande.lieu_id == Lieu.lieu_id).join(Zone, Zone.zone_id == Lieu.zone_id).group_by(Zone.zone_id).order_by(func.count(Demande.demande_id).desc()).all()
df3 = pd.DataFrame(stmt2)
print(df3)

#fermer session
session.close()