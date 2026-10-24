import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

def postresql_connect(req: str):
    conn = psycopg2.connect(
        dbname="numcity",
        user="postgres",
        password="Test_conn",
        host="localhost",
        port="5432"
    )
    df = pd.read_sql(req, conn)
    conn.close()
    return df

# 1. Emplacements par catégorie
req_categorie = """
    SELECT C.Categorie_nom, COUNT(L.Lieu_id) AS nb_emplacements
    FROM Lieu L
    JOIN Categorie C ON L.Categorie_id = C.Categorie_id
    GROUP BY C.Categorie_nom
    ORDER BY nb_emplacements DESC;
"""
df_categorie = postresql_connect(req_categorie)
print(df_categorie)

plt.figure(figsize=(6,4))
plt.bar(df_categorie['categorie_nom'], df_categorie['nb_emplacements'])
plt.title("Nombre d'emplacements par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Nombre d'emplacements")
plt.show()

# 2. Répartition par quartier (zone)
req_zone = """
    SELECT COALESCE(Z.Zone_nom, 'Hors zone') AS quartier, COUNT(L.Lieu_id) AS nb_emplacements
    FROM Lieu L
    LEFT JOIN Zone Z ON L.Zone_id = Z.Zone_id
    GROUP BY Z.Zone_nom
    ORDER BY nb_emplacements DESC;
"""
df_zone = postresql_connect(req_zone)
print(df_zone)

plt.figure(figsize=(6,6))
plt.pie(df_zone['nb_emplacements'], labels=df_zone['quartier'], autopct='%1.1f%%')
plt.title("Répartition des emplacements par quartier")
plt.show()