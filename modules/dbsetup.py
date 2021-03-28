from modules.constants import Categories
from modules.dbinsert import DBinsert


class DBsetup:
    with DBinsert() as setup:
        setup.createtables()
        setup.datacategory()
        setup.getapidata()
        setup.filterdata()
        setup.insertorupdateproducts()


DBsetup()
