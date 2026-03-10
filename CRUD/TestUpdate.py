import pymysql

connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
cursor =connection.cursor()
sql = "update user set loginId = 4 where loginId = 6"
cursor.execute(sql)
connection.commit()
connection.close()
print("data updated successfully")