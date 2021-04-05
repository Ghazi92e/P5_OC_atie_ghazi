from modules.constants import Categories
from modules.bdd.db import DB
from modules.bdd.dbsetup import DBsetup
from modules.application.home_menu import Menu


class Initapp:
    createaccount = input("Pour créer un compte entrer 1 "
                          "Pour accéder à l'application entrer 2 "
                          "Pour installer la BDD entrer 3 "
                          "Pour mettre à jour les produits entrer 4")
    if createaccount == '1':
        with DB() as d:
            user = input("Veuillez entrer un nom d'utilisateur")
            d.insertuser(user)
    elif createaccount == '3':
        with DBsetup() as u:
            u.createtables("modules/database.sql")
            u.datacategory("Category", Categories)
            u.getapidata()
            u.filterdata()
            u.insertproducts()
    elif createaccount == '4':
        with DBsetup() as u:
            u.getapidata()
            u.filterdata()
            u.insertorupdateproducts()
    elif createaccount == '2':
        with DB() as d:
            user_app = input("Entrer un nom d'utilisateur")
            d.checkuser(user_app)
            text = input("Bienvenue dans l'Openfoodfact \n"
                         "Veuillez sélectionner une option \n"
                         "1 - Quel aliment souhaitez-vous remplacer ? \n"
                         "2 - Retrouver mes aliments substitués. \n")
            while text != '1' and text != '2':
                text = input("Bienvenue dans l'Openfoodfact \n"
                             "Veuillez sélectionner une option \n"
                             "1 - Quel aliment souhaitez-vous remplacer ? \n"
                             "2 - Retrouver mes aliments substitués. \n")
            h = Menu()
            if text == '1':
                h.home_menu1(user_app)
            if text == '2':
                h.home_menu2(user_app)
            if text == 'Q':
                exit()
    else:
        print("Erreur option invalide")
