
class DBshow:
    def __init__(self, db):
        self.db = db

    def showselectrequest(self, requestsql):
        """Used to show category data table"""
        self.db.cursordb(requestsql)
        res = self.db.fetchall()
        for data in res:
            print(data)

    def showproductrequest(self, requestsql):
        """Used to show products data table"""
        self.db.cursordb(requestsql)
        res = self.db.fetchall()
        for data in res:
            print(data[0],
                  "Nom du produit:", data[1], "|",
                  "Code bar:", data[2], "|",
                  "Nutriscore:", data[3], "|",
                  "Url:", data[4], "|",
                  "Stores:", data[5])
