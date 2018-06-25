#
# May,25,2018 by Lyy

import sys
sys.path.append('./../')
import pymysql
import system_object

class connect_db(object):
    def __init__(self):
        # self.host = '172.16.124.17'
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
    def getUserMovieScore(self, user_id, movie_id):
        cursor = self.db.cursor()
        sql = 'select Score from recommend.ratings where ID=' + str(user_id) + ' and MID=' + str(movie_id)
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
        return user_id
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
        sql = "select ID,Name,password from recommend_users.user_information where ID="+str(ID)
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if name == results[0][1] and password == results[0][2]:
                return results[0][0]
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
            if sim < 1:
                if len(user):
                    return user
                else:
                    return -1
            if len(user) < 5:
                sim -= 1
                return self.getSimiUsers(user_id, sim)
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
            return ''
    def updateMovie(self, movie_id, update_sql):
        cursor = self.db.cursor()
        sql = "update recommend.movies set " + update_sql[:-1] + " where MID=" + str(movie_id)
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def getUserMovieDetail(self, movie):
        cursor = self.db.cursor()
        sql = "select Title,average_score,release_date,photo_url,local_photo_url from recommend.movies where MID=" + str(movie.Mid)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in range(len(results[0])):
                if i == 0:
                    if results[0][i] is not None:
                        movie.Name = results[0][i]
                if i == 1:
                    if results[0][i] is not None:
                        movie.average_score = results[0][i]
                elif i == 2:
                    if results[0][i] is not None:
                        movie.release_data = results[0][i]
                elif i == 3:
                    if results[0][i] is not None:
                        movie.post = results[0][i]
                elif i == 4:
                    if results[0][i] is not None:
                        movie.local_post = results[0][i]
        except:
            return -1
        return 1
    def getMovieDetail(self, movie_detail):
        cursor = self.db.cursor()
        if self.getUserMovieDetail(movie_detail.base) == -1:
            return -1
        sql = "select URL,story_line,kind,director,creator,stars,country,language,runtime,watch_time from recommend.movies where MID=" + str(movie_detail.base.Mid)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in range(len(results[0])):
                if i == 0:
                    if results[0][i] is not None:
                        movie_detail.url = results[0][i]
                elif i == 1:
                    if results[0][i] is not None:
                        movie_detail.story = results[0][i]
                elif i == 2:
                    if results[0][i] is not None:
                        movie_detail.kind = results[0][i]
                elif i == 3:
                    if results[0][i] is not None:
                        movie_detail.director = results[0][i]
                elif i == 4:
                    if results[0][i] is not None:
                        movie_detail.creator = results[0][i]
                elif i == 5:
                    if results[0][i] is not None:
                        movie_detail.stars = results[0][i]
                elif i == 6:
                    if results[0][i] is not None:
                        movie_detail.country = results[0][i]
                elif i == 7:
                    if results[0][i] is not None:
                        movie_detail.language = results[0][i]
                elif i == 8:
                    if results[0][i] is not None:
                        movie_detail.runtime = results[0][i]
                elif i == 9:
                    if results[0][i] is not None:
                        movie_detail.watch_time = results[0][i]
        except:
            return -1
        return 1
    def getMovieWatch(self, movie_id):
        cursor = self.db.cursor()
        sql = "select Score from recommend.ratings where MID=" + str(movie_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            watch_time = 0
            num_score = 0
            for i in results:
                watch_time += 1
                num_score += float(i[0])
            return watch_time,num_score
        except:
            return -1,-1
    def updateMovieWatch(self, movie_id, watch_time, average):
        cursor = self.db.cursor()
        sql = "update recommend.movies set watch_time=" + str(watch_time) + ",average_score=" + \
                str(average) + " where MID=" + str(movie_id)
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def isMovieWatch(self, user_id, movie_id):
        cursor = self.db.cursor()
        sql = "select MID from recommend.ratings where ID=" + str(user_id) + " and MID=" + str(movie_id)
        try:
            try:
                cursor.execute(sql)
            except:
                return -1
            results = cursor.fetchall()
            if results[0] is None:
                return 0
            else:
                return 1
        except:
            return 0
    def updateUserMovieScore(self, user_id, movie_id, score):
        cursor = self.db.cursor()
        sql = "update recommend.ratings set Score=" + str(score) + " where ID=" + str(user_id) + " and MID=" \
                + str(movie_id)
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def insertMovieScore(self, user_id, movie_id, score):
        cursor = self.db.cursor()
        sql = "insert into recommend.ratings(ID,MID,Score) values (" + str(user_id) + "," +\
                str(movie_id) + "," + str(score) + ")"
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def gettop100Movies(self):
        cursor = self.db.cursor()
        sql = "select MID from recommend.movies order by average_score desc"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            re = []
            for i in range(100):
                re.append(results[i][0])
            return re
        except:
            return -1
    def updateInitMovies(self, movies):
        cursor = self.db.cursor()
        sql = "update recommend.user_recommend set MID='" + movies + "' where ID=-1"
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return -1
        return 1
    def getInitMovies(self):
        cursor = self.db.cursor()
        sql = "select MID from recommend.user_recommend where ID=-1"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            results = results[0][0]
            movies = results.split(',')
            mo = []
            for i in movies:
                mo.append([int(i),0])
            return mo
        except:
            return -1
