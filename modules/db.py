# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for
# classes, files, tool windows, actions, and settings.
import mysql.connector

from modules.constants import DB_USER, DB_NAME,\
    DB_PASSWORD, DB_HOST


class DB:
    def __enter__(self):
        self.cnx = mysql.connector.connect(user=DB_USER,
                                           database=DB_NAME,
                                           password=DB_PASSWORD,
                                           host=DB_HOST)
        self.cursor = self.cnx.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()

    def selectrequest(self, select_table_name, where_field, where_data_field,
                      name_field):
        sql_select_query = f"SELECT * from {select_table_name} "
        sql_where_query = f"WHERE {where_field} = {where_data_field} "
        sql_order_query = f"ORDER BY nutriscore"
        if name_field == "select":
            return sql_select_query
        elif name_field == "where":
            return sql_select_query + sql_where_query
        elif name_field == "order":
            return sql_select_query + sql_where_query + sql_order_query

    def selectsubproductorproduct(self, product_field, cat_id, user_id):
        sql = f"""SELECT Subproduct.{product_field}, Product.name,
                Product.barcode, Product.nutriscore,
                Product.link, Product.stores
                FROM Product
                INNER JOIN Subproduct ON
                Product.id = Subproduct.{product_field}
                WHERE category_id = {cat_id} AND user_id = {user_id}"""
        return sql

    def droptable(self, table_name):
        cursor = self.cnx.cursor()
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)
        print(f"Table {table_name} deleted")

    def selectiduser(self, name):
        sql_select_query = f"SELECT id FROM User WHERE name = '{name}'"
        self.cursor.execute(sql_select_query)
        res = self.cursor.fetchone()
        self.cnx.commit()
        return res[0]
