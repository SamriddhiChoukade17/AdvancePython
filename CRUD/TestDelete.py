import pymysql

connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
cursor = connection.cursor()
sql = "delete from user where loginId = 41"
cursor.execute(sql)
connection.commit()
connection.close()
print("data deleted successfully")