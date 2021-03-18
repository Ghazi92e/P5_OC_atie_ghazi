# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for
# classes, files, tool windows, actions, and settings.
import mysql.connector


class DB:
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

    def selectproductscategory(self, category_id):
        sql_select_query = f"SELECT * from Product " \
                           f"WHERE category_id = {category_id}"
        return sql_select_query

    def selectproduct(self, product_id):
        sql_select_query = f"SELECT * from Product WHERE id = {product_id}"
        return sql_select_query

    def subproduct(self, category_id):
        sql_select_query = f"SELECT * from Product " \
                           f"WHERE category_id = {category_id} " \
                           f"ORDER BY nutriscore"
        return sql_select_query

    def selectsubproduct(self, cat_id, user_id):
        sql = f"""SELECT Subproduct.subproduct_id, Product.name,
                Product.barcode, Product.nutriscore,
                Product.link, Product.stores
                FROM Product
                INNER JOIN Subproduct ON Product.id = Subproduct.subproduct_id
                WHERE category_id = {cat_id} AND user_id = {user_id}"""
        return sql

    def selectproducttosub(self, cat_id, user_id):
        sql = f"""SELECT Subproduct.product_id, Product.name,
                Product.barcode, Product.nutriscore,
                Product.link, Product.stores
                FROM Product
                INNER JOIN Subproduct ON Product.id = Subproduct.product_id
                WHERE category_id = {cat_id} AND user_id = {user_id}"""
        return sql

    def showrequest(self, requestsql):
        self.cursor.execute(requestsql)
        res = self.cursor.fetchall()
        for data in res:
            print(data[0],
                  "Nom du produit:", data[1], "|",
                  "Code bar:", data[2], "|",
                  "Nutriscore:", data[3], "|",
                  "Url:", data[4], "|",
                  "Stores:", data[5])
        self.cnx.commit()

    def conexiondb(self):
        from mysql.connector import errorcode
        try:
            self.cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def showdata(self, table_name):
        cursor = self.cnx.cursor()
        query = f"SELECT * FROM {table_name}"

        cursor.execute(query)
        datatables = cursor.fetchall()
        for row in datatables:
            print(row)

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


if __name__ == '__main__':
    db = DB()
    # db.conexiondb()
    # db.createtables()
    # db.insertdatacategory()
    # db.getdata()
    # db.filterdata()
    # db.addnewdata()
    # db.filterdata()
    # db.insertproducts()
    # db.showdata("Product")
    # db.droptable("Product")
    # db.getname()
    # db.updatedata()
    # db.selectproductscategory(1)
    # db.showrequest(db.selectproductscategory(1))
    # db.insertsubproduct(1, 151)
    # db.insertuser("Papa")
    # db.selectiduser("Ghazi")
