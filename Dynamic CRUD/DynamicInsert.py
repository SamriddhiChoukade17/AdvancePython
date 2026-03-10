import pymysql


def testinsert():
    connection = pymysql.connect(host="localhost", port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "insert into user values('Riya', 'Pandri', 5, 105, '2007-03-25', 'Raipur')"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data inserted successfully")


def testinsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "insert into user values(%s, %s, %s, %s, %s, %s)"
    data = ('Sonu', 'Nigam', 6, 106, '1989-03-16', 'Mumbai')
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("data inserted successfully")


def testinsert3(firstName, lastName, loginId, password, dob, address):
    connection = pymysql.connect(host='localhost',port=3306,user='root', password='root',db='advancepython' )
    cursor = connection.cursor()
    sql = "INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)"
    data = (firstName, lastName, loginId, password, dob, address)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")


def testinsert4(data={}):
    firstName = data['firstName']
    lastName = data['lastName']
    loginId = data['loginId']
    password = data['password']
    dob = data['dob']
    address = data['address']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "insert into user values(%s, %s, %s, %s, %s, %s)"
    data = (firstName, lastName, loginId, password, dob, address)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("data inserted successfully")


#testinsert()
#testinsert2()
testinsert3('Shreya', 'Ghoshal', 7, '1700', '1986-06-01', 'Indore')
# testinsert4({'firstName': 'Mahi',
#              'lastName': 'Sharma',
#              'loginId': 8,
#              'password': '1800',
#              'dob': '2001-02-03',
#              'address': 'Delhi'})
