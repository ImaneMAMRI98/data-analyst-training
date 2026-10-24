import psycopg2


def postresql_connect(req: str):
    # Connexion à la base de données
    conn = psycopg2.connect(
        dbname="numcity",
        user="postgres",
        password="Test_conn",
        host="localhost",
        port="5432"
    )

    # Création d'un curseur
    cursor = conn.cursor()

    # Exécution d'une requête SQL
    # Exécution d'une requête SQL
    cursor.execute(req)
    rows = cursor.fetchall()
    # Fermeture de la connexion
    cursor.close()
    conn.close()
    return rows

req = "SELECT D.Demande_id,D.Demande_type, D.Demande_description, D.Demande_date,C.User_name AS Citoyen,C.User_email,L.Lieu_id FROM Demande D JOIN Citoyen C ON D.User_id = C.User_id JOIN Lieu L ON D.Lieu_id = L.Lieu_id ORDER BY D.Demande_date DESC;"
print(postresql_connect(req))


req1 = "SELECT * FROM categorie;"
print(postresql_connect(req1))

req2 = "SELECT * FROM Citoyen;"
print(postresql_connect(req2))

req3 = "SELECT * FROM demande;"
print(postresql_connect(req3))

req4 = "SELECT * FROM lieu;"
print(postresql_connect(req4))

req5 = "SELECT * FROM zone;"
print(postresql_connect(req5))
        