import mysql.connector

from main import DB


class Createuser:

    def __init__(self):

        self.cnx = mysql.connector.connect(user='ghazi',
                                           database='elevage',
                                           password='Liban',
                                           host='localhost')
        self.cursor = self.cnx.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()

    def insertuser(self, user_name):
        try:
            add_user = ("""INSERT INTO User
                                   (name)
                                 VALUES (%(name)s)""")
            user_data = {
                'name': user_name,
            }
            self.cursor.execute(add_user, user_data)
            self.cnx.commit()
            print(f"Le nom d'utilisateur {user_name} a été crée")
        except mysql.connector.errors.IntegrityError:
            print("Ce nom d'utilisateur existe déjà")

    def checkuser(self, user_name):
        sql_select_query = f"SELECT name from User WHERE name = '{user_name}'"
        self.cursor.execute(sql_select_query)
        res = self.cursor.fetchall()
        if res:
            print("Le nom d'utilisateur est valide")
        else:
            print("Le nom d'utilisateur est invalide")
            exit()

# user = Createuser()
# username = input("Veuillez entrer un nom d'utilisateur:")
# user.insertuser(username)
# user.checkuser("Ghazi")
