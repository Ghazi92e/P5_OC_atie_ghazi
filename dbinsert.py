import mysql.connector
import requests

from constants import Categories


class DBinsert:
    def __init__(self):

        self.cnx = mysql.connector.connect(user='ghazi',
                                           database='elevage',
                                           password='Liban',
                                           host='localhost')
        self.cursor = self.cnx.cursor()
        self.products = {}

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()

    def createtables(self):
        with open("database.sql") as sqlfile:
            content = sqlfile.read()
            sqlcommands = content.split(';')
            cursor = self.cnx.cursor()
            for tables in sqlcommands:
                cursor.execute(tables)
            print("Table created")

    def datacategory(self):
        add_category = ("INSERT INTO Category "
                        "(id, name) "
                        "VALUES (%(id)s, %(name)s)")
        id = self.cursor.lastrowid
        for name in Categories:
            data_category = {
                                'id': id,
                                'name': name,
                            },
            self.cursor.executemany(add_category,
                                    data_category)
            self.cnx.commit()
            print(self.cursor.rowcount, "Record inserted successfully "
                                        "into Laptop table")

    def getapidata(self):
        for category in Categories:
            r = requests.get(
                'https://fr.openfoodfacts.org/cgi/search.pl',
                params={
                    'json': 'true',
                    'search_terms': category,
                    'search_tag': 'categories',
                    'fields': 'generic_name_fr,code,'
                              'nutrition_grades,url,stores',
                    'tag_contains_0': 'contains',
                    'page_size': 30,
                    'page': 1,
                },
            )
            res = r.json()
            self.products[category] = res["products"]

    def filterdata(self):
        for key in Categories:
            for data in self.products[key]:
                try:
                    if data['stores'] == '':
                        data.pop("stores")
                    if data['generic_name_fr'] == '':
                        data.pop("generic_name_fr")
                except KeyError:
                    pass

    def insertproducts(self):
        add_product = ("""INSERT INTO Product
                       (id, name, barcode, link, nutriscore,
                       stores, category_id)
                       VALUES (%(id)s, %(name)s, %(barcode)s,
                       %(link)s, %(nutriscore)s, %(stores)s,
                       %(category_id)s)""")

        id = self.cursor.lastrowid
        selectcatid = """SELECT * from Category"""
        self.cursor.execute(selectcatid)
        datatables = self.cursor.fetchall()
        for d in datatables:
            for prod in self.products[d[1]]:
                try:
                    data_product = {
                        'id': id,
                        'name': prod['generic_name_fr'],
                        'stores': prod['stores'],
                        'barcode': prod['code'],
                        'link': prod['url'],
                        'nutriscore': prod['nutrition_grades'],
                        'category_id': d[0],
                    }
                    self.cursor.execute(add_product, data_product)
                    self.cnx.commit()
                except KeyError:
                    pass

    def updatedata(self):
        for key in Categories:
            for prod in self.products[key]:
                try:
                    sql_update_query = f"""UPDATE Product SET name = %s,
                                        barcode = %s, nutriscore = %s,
                                        link = %s,
                                        stores = %s WHERE barcode = %s"""
                    val = (prod['generic_name_fr'], prod['code'],
                           prod['nutrition_grades'], prod['url'],
                           prod['stores'], prod['code'])
                    self.cursor.execute(sql_update_query, val)
                    self.cnx.commit()
                except KeyError:
                    pass

    def insertsubproduct(self, subproduct_id, product_id, user_id):
        add_product = ("""INSERT INTO Subproduct
                               (subproduct_id, product_id, user_id)
                             VALUES (%(subproduct_id)s,
                             %(product_id)s, %(user_id)s) """)

        data_product = {
            'subproduct_id': subproduct_id,
            'product_id': product_id,
            'user_id': user_id,
        }
        self.cursor.execute(add_product, data_product)
        self.cnx.commit()


insert = DBinsert()
# insert.createtables()
# insert.datacategory()
insert.getapidata()
insert.filterdata()
insert.insertproducts()
# insert.updatedata()
