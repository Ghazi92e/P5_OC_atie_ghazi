from dbinsert import DBinsert
from main import DB


class Menu:
    def home_menu(self):

        text = input("Bienvenue dans l'Openfoodfact \n"
                     "Veuillez sélectionnez une option \n"
                     "1 - Quel aliment souhaitez-vous remplacer ? \n"
                     "2 - Retrouver mes aliments substitués \n")

        if text == "1":
            c = DB()
            user = input("Entrer votre nom d'utilisateur")
            print("Sélectionnez la catégorie")
            c.showdata("Category")
            cat = input()
            c.showrequest(c.selectproductscategory(cat))
            selectproduct = input("Veuillez sélectionnez un aliment \n")
            print("Voici le produit que vous avez sélectionnez:")
            c.showrequest(c.selectproduct(selectproduct))
            print("Produit de substitut:")
            c.showrequest(c.subproduct(cat))
            insertsub = input("Selectionnez un substitut")
            i = DBinsert()
            i.insertsubproduct(insertsub, selectproduct, c.selectiduser(user))

        elif text == "2":
            c = DB()
            user = input("Entrer votre nom d'utilisateur")
            c.showdata("Category")
            cat_id = input("Veuillez sélectionnez une categorie")
            print("Produits de substitut")
            c.showrequest(c.selectsubproduct(cat_id, c.selectiduser(user)))
            print("Aliment(s) substitué(s)")
            c.showrequest(c.selectproducttosub(cat_id, c.selectiduser(user)))


r = Menu()
r.home_menu()
