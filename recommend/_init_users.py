#
#
# init user account
# May,29,2018 by Lyy

import connect_db

def insert_user(name, password):
    mysql = connect_db.connect_db()
    if mysql.insert_user(name, password) == -1:
        mysql.close()
        return -1
    mysql.close()
    return 1

def isHaveName(name):
    mysql = connect_db.connect_db()
    if mysql.isHaveName(name):
        mysql.close()
        return 1
    mysql.close()
    return 0

def accessCheck(name, password):
    mysql = connect_db.connect_db()
    sign = mysql.accessCheck(name,password)
    mysql.close()
    return sign

#for i in range(1,944):
#    if insert_user(str(i),str(i)) == -1:
#        print('wrong')
#        break
