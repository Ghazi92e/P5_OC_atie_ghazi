from createuser import Createuser
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
            u = Createuser()
            user = input("Entrer votre nom d'utilisateur")
            u.checkuser(user)
            print("Sélectionnez la catégorie")
            c.showdata("Category")
            cat = input()
            c.showrequest(c.selectcategoryorproduct("category_id", cat))
            selectproduct = input("Veuillez sélectionnez un aliment \n")
            print("Voici le produit que vous avez sélectionnez:")
            c.showrequest(c.selectcategoryorproduct("id", selectproduct))
            print("PRODUITS DE SUBSTITUS:")
            c.showrequest(c.subproduct(cat))
            insertsub = input("Selectionnez un substitut")
            i = DBinsert()
            i.insertsubproduct(insertsub, selectproduct, c.selectiduser(user))

        elif text == "2":
            c = DB()
            u = Createuser()
            user = input("Entrer votre nom d'utilisateur")
            u.checkuser(user)
            c.showdata("Category")
            cat_id = input("Veuillez sélectionnez une categorie")
            print("Produits de substitut:")
            c.showrequest(c.selectsubproductorproduct("subproduct_id", cat_id, c.selectiduser(user)))
            print("Aliment(s) substitué(s):")
            c.showrequest(c.selectsubproductorproduct("product_id", cat_id, c.selectiduser(user)))

r = Menu()
r.home_menu()
