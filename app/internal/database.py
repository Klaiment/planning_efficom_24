import mariadb

try:
    connection = mariadb.connect(
        user="usertest",
        password="mysecurepassword",
        host="database_maria",
        port=3306,
        database="planning"
    )
    print("Connexion réussie !")
except mariadb.Error as err:
    print(f"Erreur lors de la connexion à la base de données : {err}")

def query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
<<<<<<< HEAD
=======
    connection.commit()
>>>>>>> 97a92ec7e2b8bff6f71d1f3a19d3ce0464ff8b8f
    cursor.close()  # Fermez le curseur
    return result

def execute(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()  # Fermez le curseur
        return 1
    except Exception as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")
<<<<<<< HEAD
        return 0
=======
        return 0

>>>>>>> 97a92ec7e2b8bff6f71d1f3a19d3ce0464ff8b8f
