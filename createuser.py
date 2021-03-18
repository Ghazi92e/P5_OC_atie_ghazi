import mysql.connector


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
                                   (id, name)
                                 VALUES (%(id)s, %(name)s)""")
            id = self.cursor.lastrowid
            user_data = {
                'id': id,
                'name': user_name,
            }
            self.cursor.execute(add_user, user_data)
            self.cnx.commit()
            print(f"Nom d'utilisateur {user_name} a été crée")
        except mysql.connector.errors.IntegrityError:
            print("Ce nom d'utilisateur existe déjà")


user = Createuser()
username = input("Veuillez entrer un nom d'utilisateur:")
user.insertuser(username)
