from modules.db import DB


class DBshow(DB):
    def showselectrequest(self, requestsql):
        self.cursor.execute(requestsql)
        res = self.cursor.fetchall()
        for data in res:
            print(data)
        self.cnx.commit()

    def showproductrequest(self, requestsql):
        self.cursor.execute(requestsql)
        res = self.cursor.fetchall()
        for data in res:
            print(data[0],
                  "Nom du produit:", data[1], "|",
                  "Code bar:", data[2], "|",
                  "Nutriscore:", data[3], "|",
                  "Url:", data[4], "|",
                  "Stores:", data[5])
        self.cnx.commit()
