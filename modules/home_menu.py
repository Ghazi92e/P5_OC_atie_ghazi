from modules.createuser import Createuser
from modules.db import DB
from modules.dbinsert import DBinsert
from modules.dbshow import DBshow


class Menu(DB):
    def __init__(self):
        """Used to check if user are valide"""
        with Createuser() as u:
            self.user = input("Entrer un nom d'utilisateur")
            u.checkuser(self.user)

    def home_menu1(self):
        with DBinsert() as c:
            """Used to manage the first part of the menu"""
            with DBshow() as s:
                print("Sélectionner la catégorie")
                s.showselectrequest(c.selectrequest("Category", "None",
                                                    "None", "select"))
                cat = input()
                s.showproductrequest(c.selectrequest("Product", "category_id",
                                                     cat, "where"))
                selectproduct = input("Veuillez sélectionner un aliment \n")
                print("Voici le produit que vous avez sélectionnez:")
                s.showproductrequest(c.selectrequest("Product", "id",
                                                     selectproduct, "where"))
                print("PRODUITS DE SUBSTITUS:")
                s.showproductrequest(c.selectrequest("Product", "category_id",
                                                     cat, "order"))
                insertsub = input("Selectionner un substitut")
                c.insertsubproduct(insertsub, selectproduct,
                                   c.selectiduser(self.user))
                print("Vos informations ont bien été sauvegardées")
                text = input("Entrer 2 pour retrouver vos aliments substitués"
                             " ou Q pour quitter")
                if text == '2':
                    self.home_menu2()

    def home_menu2(self):
        with DBinsert() as c:
            """Used to manage the second part of the menu"""
            with DBshow() as s:
                s.showselectrequest(c.selectrequest("Category", "None",
                                                    "None", "select"))
                cat_id = input("Veuillez sélectionner une categorie")
                print("Produits de substitut:")
                s.showproductrequest(c.selectsubproductorproduct(
                    "subproduct_id", cat_id, c.selectiduser(self.user)))
                print("Aliment(s) substitué(s):")
                s.showproductrequest(c.selectsubproductorproduct(
                    "product_id", cat_id, c.selectiduser(self.user)))
                text = input("Entrer 1 pour sélectionner un aliment ou Q pour quitter")
                if text == '1':
                    self.home_menu1()

