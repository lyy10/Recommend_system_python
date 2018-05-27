#

import pymysql

def connectdb():
    print('begain to connect mysql service')
    db = pymysql.connect('localhost', 'root', '1010', 'lyy')
    print('seccussful')
    return db

def querydb(db):
    cursor = db.cursor()
    sql = 'select * from ratings'
    try:
        cursor.execute(sql)
    #try:
        results = cursor.fetchall()
        i = 0
        for row in results:
            ID = row[0]
            MID = row[1]
            Grade = row[2]
            Time = row[3]
            print("ID: %d, MID: %d, Grade: %f, Time: %s" %(ID,MID,Grade,Time))
            i += 1
            if i == 20:
                break
    except:
        print("Error: unable to fecth data")
db = connectdb()
querydb(db)
