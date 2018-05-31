#
# May,25,2018 by Lyy

import sys
sys.path.append('./../')
import pymysql
import system_object

class connect_db(object):
    def __init__(self):
        self.host = '172.16.124.17'
        self.port = '3306'
        self.user = 'recommend'
        self.password = 'recommend'
        self.table = 'recommend'
        self.db = pymysql.connect(self.host, self.user, self.password, self.table)
    def close(self):
        self.db.close()

    def getNumUser(self):
        cursor = self.db.cursor()
        sql = 'select count(ID) from recommend_users.user_information'
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results[0][0]
        except:
            return -1
    def getUserMovies(self, user_id):
        cursor = self.db.cursor()
        sql = 'select MID,Score from recommend.ratings where ID=' + str(user_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            #print(results)
            movies = []
            for row in results:
                movie = system_object.Movies()
                movie.Mid = row[0]
                movie.user_score = row[1]
                movies.append(movie)
            return movies
        except:
            return -1
    def updateSimilarity(self, user_id, i, sim, sim1, sim2, sim3):
        cursor = self.db.cursor()
        if user_id < i:
            sql = "insert into recommend.user_To_user_Similarity  values ("+str(user_id)+","+\
                    str(i)+","+str(sim)+","+str(sim1)+","+str(sim2)+","+str(sim3)+")"
        else:
            sql = "insert into recommend.user_To_user_Similarity  values ("+str(i)+","+\
                    str(user_id)+","+str(sim)+","+str(sim1)+","+str(sim2)+","+str(sim3)+")"
        try:
            cursor.execute(sql)
            self.db.commit()
            return 1
        except:
            db.rollback()
            return -1
    def insert_user(self, name, password):
        if self.isHaveName(name):
            return -1
        user_id = self.getNumUser() + 1
        cursor = self.db.cursor()
        sql = "insert into recommend_users.user_information values ("+str(user_id)+",'"+name+"','"+\
                password+"',"+"NOW(),NOW(),NOW())"
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def isHaveName(self, name):
        cursor = self.db.cursor()
        sql = "select ID,Name from recommend_users.user_information"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                if name == i[1]:
                    return i[0]
            return 0
        except:
            return 0
    def accessCheck(self, name, password):
        ID = self.isHaveName(name)
        if not ID:
            return -1
        sql = "select Name,password from recommend_users.user_information where ID="+str(ID)
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if name == results[0][0] and password == results[0][1]:
                return 1
            else:
                return 0
        except:
            return 0
    def getSimiUsers(self, user_id, sim):
        cursor = self.db.cursor()
        sql = "select ID1,ID2 from recommend.user_To_user_Similarity where (ID1="+str(user_id)+\
                " or ID2="+str(user_id)+") and Similarity>"+str(sim)+" order by Similarity desc"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            user = []
            for row in results:
                if row[0] == user_id:
                    user.append(row[1])
                else:
                    user.append(row[0])
            return user
        except:
            # auto. adapt WoW 临时想到
            sim -= 0.1
            if sim > 0:
                return self.getSimiUsers(user_id,sim)
            else:
                return -1
    def getTestMovies(self, user_id):
        cursor = self.db.cursor()
        sql = 'select MID,Score from recommend.test_user where ID=' + str(user_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            movies = []
            for row in results:
                movies.append([row[0],row[1]])
            return movies
        except:
            return -1
    def getMoviesName(self, movie_id):
        cursor = self.db.cursor()
        sql = 'select Title from recommend.movies where MID=' + str(movie_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results[0][0]
        except:
            return 'null'
    def getUserName(self, user_id):
        cursor = self.db.cursor()
        sql = 'select Name from recommend_users.user_information where ID=' + str(user_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results[0][0]
        except:
            return 'null'
