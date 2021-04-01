from modules.dbinsert import DBinsert


class DBsetup:
    """Used to setup DB"""
    with DBinsert() as setup:
        setup.createtables()
        setup.datacategory()
        setup.getapidata()
        setup.filterdata()
        setup.insertproducts()


DBsetup()
