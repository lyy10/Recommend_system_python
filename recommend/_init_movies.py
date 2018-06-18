#
# Movies related functions
# June,17 2018 By Lyy

import sys
sys.path.append('./../')
sys.path.append('./../spider/')
import system_object
import connect_db
import _spider
import tqdm

def getMovieDetail(movie_id):
    mysql = connect_db.connect_db()
    movie_detail = system_object.MoviesDetail()
    movie_detail.base.Mid = movie_id
    if mysql.getMovieDetail(movie_detail) == -1:
        mysql.close()
        return 0
    #_spider.movies_detail_view(movie_detail)
    mysql.close()
    return movie_detail

def maintainAverageScore(movie_id):
    mysql = connect_db.connect_db()
    watch_time, num_score = mysql.getMovieWatch(movie_id)
    #print(watch_time,num_score)
    if watch_time == -1:
        mysql.close()
        return -1
    elif watch_time == 0:
        if mysql.updateMovieWatch(movie_id, watch_time, 0) == -1:
            mysql.close()
            return -1
        else:
            mysql.close()
            return 1
    average = num_score/watch_time
    if mysql.updateMovieWatch(movie_id, watch_time, average) == -1:
        mysql.close()
        return -1
    mysql.close()
    return 1

def insertMovieScore(user_id, movie_id, movie_score):
    mysql = connect_db.connect_db()
    sign = mysql.isMovieWatch(user_id,movie_id)
    if sign  == -1:
        mysql.close()
        return -1
    elif sign == 0:
        if mysql.insertMovieScore(user_id,movie_id,movie_score) == -1:
            mysql.close()
            return -1
    else:
        if mysql.updateUserMovieScore(user_id,movie_id,movie_score) == -1:
            mysql.close()
            return -1
    mysql.close()
    return 1

def getUserHaveWatch(user_id):
    mysql = connect_db.connect_db()
    user = system_object.User(user_id)
    user.name = mysql.getUserName(user_id)
    have_watch = mysql.getUserMovies(user_id)
    for i in range(len(have_watch)):
        mysql.getUserMovieDetail(have_watch[i])
    user.movies = have_watch
    mysql.close()
    return user

if __name__=='__main__':
    #print(maintainAverageScore(599))
    #for i in tqdm.tqdm(range(1,1683)):
    #    if maintainAverageScore(i) == -1:
    #        print('错误: ',i)
    #print('Congratulations')
    #pbar = tqdm.tqdm([599,711,814,830,852,857,1156,1236,1309,1310,1320,1343,1648,1364\
    #                  ,1373,1457,1458,1492,1493,1498,1505,1520,1533,1536,1543,1557\
    #                  ,1561,1562,1563,1565,1582,1586])
    #for i in pbar:
    #    if maintainAverageScore(i) == -1:
    #        print('错误: ',i)
    #print(insertMovieScore(1,1,5))
    #print(getUserHaveWatch(1).movies[0].user_score)
    pass
