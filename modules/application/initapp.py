from modules.constants import Categories
from modules.bdd.db import DB
from modules.bdd.dbsetup import DBsetup
from modules.application.home_menu import Menu


class Initapp:
    def mainapp(self):
        """Manage main application"""
        createaccount = input("Pour créer un compte entrer 1 "
                              "Pour accéder à l'application entrer 2 "
                              "Pour installer la BDD entrer 3 "
                              "Pour mettre à jour les produits entrer 4")
        if createaccount == '1':
            with DB() as db:
                user = input("Veuillez entrer un nom d'utilisateur")
                db.insertuser(user)
        elif createaccount == '3':
            with DB() as db:
                dbsetup = DBsetup(db)
                dbsetup.createtables("modules/database.sql")
                dbsetup.datacategory("Category", Categories)
                dbsetup.getapidata()
                dbsetup.filterdata()
                dbsetup.insertproducts()
        elif createaccount == '4':
            with DB() as db:
                dbsetup = DBsetup(db)
                dbsetup.getapidata()
                dbsetup.filterdata()
                dbsetup.insertorupdateproducts()
        elif createaccount == '2':
            h = Menu()
            user_app = input("Entrer un nom d'utilisateur")
            h.check_userapp(user_app)
            text = input("Bienvenue dans l'Openfoodfact \n"
                         "Veuillez sélectionner une option \n"
                         "1 - Quel aliment souhaitez-vous remplacer ? \n"
                         "2 - Retrouver mes aliments substitués. \n")
            while text != '1' and text != '2':
                text = input("Bienvenue dans l'Openfoodfact \n"
                             "Veuillez sélectionner une option \n"
                             "1 - Quel aliment souhaitez-vous "
                             "remplacer ? \n"
                             "2 - Retrouver mes aliments substitués. \n")
            if text == '1':
                h.home_menu1(user_app)
            if text == '2':
                h.home_menu2(user_app)
            if text == 'Q':
                exit()
        else:
            print("Erreur option invalide")
