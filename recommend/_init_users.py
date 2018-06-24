#
#
# init user account
# May,29,2018 by Lyy
# May,31,2018 updated by Ch
import sys
sys.path.append('./../Recommend_system_python')
import connect_db

def insert_user(name, password):
    mysql = connect_db.connect_db()
    re = mysql.insert_user(name, password)
    mysql.close()
    return re

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

def getUserName(user_id):
    mysql = connect_db.connect_db()
    sign = mysql.getUserName(user_id)
    mysql.close()
    if sign is '':
        return 0
    return sign

#for i in range(1,944):
#    if insert_user(str(i),str(i)) == -1:
#        print('wrong')
#        break
