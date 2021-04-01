# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for
# classes, files, tool windows, actions, and settings.
from modules.createuser import Createuser
from modules.dbinsert import DBinsert
from modules.home_menu import Menu

with DBinsert() as u:
    """Main menu"""
    createaccount = input("Pour créer un compte entrer 1"
                          " pour accéder à l'application entrer 2")

    if createaccount == '1':
        with Createuser() as create:
            user = input("Veuillez entrer un nom d'utilisateur")
            create.insertuser(user)
    elif createaccount == '2':
        with Menu() as u:
            text = input("Bienvenue dans l'Openfoodfact \n"
                         "Veuillez sélectionner une option \n"
                         "1 - Quel aliment souhaitez-vous remplacer ? \n"
                         "2 - Retrouver mes aliments substitués. \n")
            while text != '1' and text != '2':
                text = input("Bienvenue dans l'Openfoodfact \n"
                             "Veuillez sélectionner une option \n"
                             "1 - Quel aliment souhaitez-vous remplacer ? \n"
                             "2 - Retrouver mes aliments substitués. \n")
            if text == '1':
                u.home_menu1()
            if text == '2':
                u.home_menu2()
            if text == 'Q':
                exit()
    else:
        print("Erreur option invalide")
