import folium
from sqlalchemy import create_engine, text,Column, Integer, String,Text, TIMESTAMP, ForeignKey, Numeric, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import pandas as pd
from scipy.spatial import ConvexHull

icons_list = {
    "Fontaine à eau" : 'tint',
    "Parking vélos" : 'road',#
    "Toilettes publiques" : '',#
    "Banc public" : 'pause',#
    "Poubelle / corbeille de tri" : 'trash',
    "Éclairage public" : 'flash',#
    "Aire de jeux" : 'star',#
    "NULL" : 'info-sign'
}

#connexion a la base ...username:mdp@serveur/nom de la base
engine = create_engine('postgresql://postgres:Test_conn@localhost/numcity')
# creer une classe (base) parent pour que les classes vont heriter pour devenir des tables ORM
Base = declarative_base()
class Categorie (Base):
    __tablename__ = 'categorie'
    categorie_id = Column(String(50), primary_key=True)
    categorie_nom = Column(String(50), nullable=False)

class Zone (Base):
    __tablename__ = 'zone'
    zone_id = Column(String(50), primary_key=True)
    zone_nom = Column(String(50), nullable=False)

class Lieu(Base):
    __tablename__ = 'lieu'
    lieu_id = Column(String(50), primary_key=True)
    lieu_latitude = Column(Numeric(9,6), nullable=False)
    lieu_longtitude = Column(Numeric(9,6), nullable=False)
    zone_id = Column(String(50), ForeignKey('zone.zone_id'), nullable=False)
    categorie_id = Column(String(50), ForeignKey('categorie.categorie_id'), nullable=False)

# creation d'une session pour interoger la base
Session = sessionmaker(bind=engine)
session = Session()
req = session.query(
                    Lieu.lieu_id,
                    Lieu.lieu_latitude,
                    Lieu.lieu_longtitude,
                    Zone.zone_nom,
                    Categorie.categorie_nom
                    ).join(Zone, Zone.zone_id == Lieu.zone_id).join(Categorie, Categorie.categorie_id == Lieu.categorie_id)


df = pd.DataFrame(req)

#fermer session
session.close()

df['lieu_latitude'] = df['lieu_latitude'].astype(float)
df['lieu_longtitude'] = df['lieu_longtitude'].astype(float)

# --- Carte de base ---
m = folium.Map(location=[44.5586, 4.7508], zoom_start=13, tiles='CartoDB positron')

# --- Polygones par zone ---
for zone_nom, group in df.groupby('zone_nom'):
    points = group[['lieu_latitude', 'lieu_longtitude']].values
    if len(points) < 3:
        continue  # pas assez de points pour calculer une enveloppe
    hull = ConvexHull(points)
    polygon_coords = points[hull.vertices].tolist()

    folium.Polygon(
        locations=polygon_coords,
        color='green',
        weight=2,
        fill=True,
        fill_opacity=0.1,
        tooltip=zone_nom
    ).add_to(m)

# --- Marqueurs groupés par catégorie (pour le filtre) ---
categories = df['categorie_nom'].unique()
groups = {cat: folium.FeatureGroup(name=cat) for cat in categories}

for _, row in df.iterrows():
    folium.Marker(
        location=[row['lieu_latitude'], row['lieu_longtitude']],
        popup=f"{row['lieu_id']} ({row['categorie_nom']})",
        icon=folium.Icon(icon=icons_list[row['categorie_nom']]),
    ).add_to(groups[row['categorie_nom']])

for g in groups.values():
    g.add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

# --- Sauvegarde ---
m.save('index.html')