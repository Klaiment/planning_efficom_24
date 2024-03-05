import mariadb

try:
    connection = mariadb.connect(
        user="usertest",
        password="mysecurepassword",
        host="database_maria",
        port=3306,
        database="planning"
    )

    def query(query):
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    def execute(query):
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        return 1

except mariadb.Error as err:
    print(f"Erreur lors de la connexion à la base de données : {err}")
