import mysql.connector

from modules.createuser import Createuser
from dbinsert import DBinsert
from modules.db import DB


class Menu:
    def __init__(self):
        with Createuser() as u:
            self.user = input("Entrer un nom d'utilisateur")
            u.checkuser(self.user)

    def __enter__(self):
        self.cnx = mysql.connector.connect(user='ghazi',
                                           database='elevage',
                                           password='Liban',
                                           host='localhost')
        self.cursor = self.cnx.cursor()
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.cursor.close()

    def home_menu1(self):
        with DB() as c:
            print("Sélectionnez la catégorie")
            c.showselectrequest(c.selectrequest("Category", "None", "None", "select"))
            cat = input()
            c.showproductrequest(c.selectrequest("Product", "category_id", cat, "where"))
            selectproduct = input("Veuillez sélectionnez un aliment \n")
            print("Voici le produit que vous avez sélectionnez:")
            c.showproductrequest(c.selectrequest("Product", "id", selectproduct, "where"))
            print("PRODUITS DE SUBSTITUS:")
            c.showproductrequest(c.selectrequest("Product", "category_id", cat, "order"))
        with DBinsert() as i:
            insertsub = input("Selectionnez un substitut")
            i.insertsubproduct(insertsub, selectproduct, c.selectiduser(self.user))

    def home_menu2(self):
        with DB() as c:
            c.showselectrequest(c.selectrequest("Category", "None", "None", "select"))
            cat_id = input("Veuillez sélectionnez une categorie")
            print("Produits de substitut:")
            c.showproductrequest(c.selectsubproductorproduct("subproduct_id", cat_id, c.selectiduser(self.user)))
            print("Aliment(s) substitué(s):")
            c.showproductrequest(c.selectsubproductorproduct("product_id", cat_id, c.selectiduser(self.user)))
