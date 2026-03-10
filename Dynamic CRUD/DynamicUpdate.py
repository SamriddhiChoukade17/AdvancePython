import pymysql

def testupdate1():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "update user set firstName = 'Rohan' where loginId = 2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data updated successfully")