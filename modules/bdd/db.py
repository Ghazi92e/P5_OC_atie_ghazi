# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for
# classes, files, tool windows, actions, and settings.
import mysql.connector

from modules.constants import DB_USER, DB_NAME, \
    DB_PASSWORD, DB_HOST


class DB:
    def __enter__(self):
        """Open the connexion to the DB"""
        self.cnx = mysql.connector.connect(user=DB_USER,
                                           database=DB_NAME,
                                           password=DB_PASSWORD,
                                           host=DB_HOST)
        self.cursor = self.cnx.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connexion to the DB"""
        self.cursor.close()

    def selectrequest(self, select_table_name, where_field, where_data_field,
                      name_field):
        """Select product from DB"""
        sql_select_query = f"SELECT * from {select_table_name} "
        sql_where_query = f"WHERE {where_field} = {where_data_field} "
        sql_order_query = f"AND nutriscore != 'e' ORDER BY RAND() LIMIT 1"
        if name_field == "select":
            return sql_select_query
        elif name_field == "where":
            return sql_select_query + sql_where_query
        elif name_field == "order":
            return sql_select_query + sql_where_query + sql_order_query

    def selectsubproductorproduct(self, product_field, cat_id, user_id):
        """Select subproduct or product"""
        sql = f"""SELECT Subproduct.{product_field}, Product.name,
                Product.barcode, Product.nutriscore,
                Product.link, Product.stores
                FROM Product
                INNER JOIN Subproduct ON
                Product.id = Subproduct.{product_field}
                WHERE category_id = {cat_id} AND user_id = {user_id}"""
        return sql

    def selectiduser(self, name):
        """Select the user id"""
        sql_select_query = f"SELECT id FROM User WHERE name = '{name}'"
        self.cursordb(sql_select_query)
        res = self.cursor.fetchone()
        self.commit()
        return res[0]

    def insertsubproduct(self, subproduct_id, product_id, user_id):
        """Used to insert a substitute product in DB"""
        add_product = ("""INSERT INTO Subproduct
                               (subproduct_id, product_id, user_id)
                             VALUES (%(subproduct_id)s,
                             %(product_id)s, %(user_id)s) """)

        data_product = {
            'subproduct_id': subproduct_id,
            'product_id': product_id,
            'user_id': user_id,
        }
        self.cursordb(add_product, data=data_product)
        self.commit()

    def insertuser(self, user_name):
        """Used to insert user in DB"""
        try:
            add_user = ("""INSERT INTO User
                                   (name)
                                 VALUES (%(name)s)""")
            user_data = {
                'name': user_name,
            }
            self.cursordb(add_user, data=user_data)
            self.commit()
            print(f"Le nom d'utilisateur {user_name} a été crée")
        except mysql.connector.errors.IntegrityError:
            print("Ce nom d'utilisateur existe déjà")

    def checkuserdb(self, user_name):
        """Used to check if username already exists in DB"""
        sql_select_query = f"SELECT name from User WHERE name = '{user_name}'"
        self.cursordb(sql_select_query)
        res = self.fetchall()
        if res:
            print("Le nom d'utilisateur est valide")
        else:
            print("Le nom d'utilisateur est invalide")
            exit()

    def cursordb(self, requestsql, data=None):
        """open a database cursor"""
        if data:
            self.cursor.execute(requestsql, data)
        else:
            self.cursor.execute(requestsql)

    def fetchall(self):
        """display a database request"""
        return self.cursor.fetchall()

    def commit(self):
        """execute a database request"""
        return self.cnx.commit()
