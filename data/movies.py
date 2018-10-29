
def createTable(struct, dbconnect):
    try:
        pass
    except Exception as e:
        print e


def insertDb(data, dbconnect):
    try:
        db = dbconnect()
        cursor = db.cursor()
        cursor.execute("""
        INSERT INTO nameoftable(nameofcolumn) \
        VALUES (%s) """, (data))
        cursor.close()
    except Exception as e:
        print e