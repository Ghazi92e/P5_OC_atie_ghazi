from modules.bdd.db import DB
from modules.bdd.dbshow import DBshow


class Menu:
    def home_menu1(self, user):
        with DB() as db:
            """Used to manage the first part of the menu"""
            db_show = DBshow(db)
            print("Sélectionner la catégorie")
            db_show.showselectrequest(db.selectrequest
                                      ("Category", "None",
                                       "None", "select"))
            cat = input()
            db_show.showproductrequest(db.selectrequest
                                       ("Product", "category_id",
                                        cat, "where"))
            selectproduct = input("Veuillez sélectionner un aliment \n")
            print("Voici le produit que vous avez sélectionnez:")
            db_show.showproductrequest(db.selectrequest
                                       ("Product", "id",
                                        selectproduct, "where"))
            print("PRODUITS DE SUBSTITUS:")
            db_show.showproductrequest(db.selectrequest
                                       ("Product", "category_id",
                                        cat, "order"))
            insertsub = input("Selectionner un substitut")
            db.insertsubproduct(insertsub, selectproduct,
                                db.selectiduser(user))
            print("Vos informations ont bien été sauvegardées")
            text = input("Entrer 2 pour retrouver vos aliments substitués"
                         " ou Q pour quitter")
            if text == '2':
                self.home_menu2(user)

    def home_menu2(self, user):
        with DB() as db:
            """Used to manage the second part of the menu"""
            db_show = DBshow(db)
            db_show.showselectrequest(db.selectrequest("Category", "None",
                                                       "None", "select"))
            cat_id = input("Veuillez sélectionner une categorie")
            print("Produits de substitut:")
            db_show.showproductrequest(db.selectsubproductorproduct(
                "subproduct_id", cat_id, db.selectiduser(user)))
            print("Aliment(s) substitué(s):")
            db_show.showproductrequest(db.selectsubproductorproduct(
                "product_id", cat_id, db.selectiduser(user)))
            text = input("Entrer 1 pour sélectionner un aliment "
                         "ou Q pour quitter")
            if text == '1':
                self.home_menu1(user)
