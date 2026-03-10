import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
cursor = connection.cursor()
# insert into user values(firstName, lastName, loginId, password, dob, address)
sql = "insert into user values('Abhi', 'singh', 6, '105', '2004-05-26', 'Indore')"
cursor.execute(sql)
connection.commit()
connection.close()
print('data inserted successfully')
