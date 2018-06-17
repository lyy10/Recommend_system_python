#
# Movies related functions
# June,17 2018 By Lyy

import sys
sys.path.append('./../')
sys.path.append('./../spider/')
import system_object
import connect_db
import _spider

def getMovieDetail(movie_id):
    mysql = connect_db.connect_db()
    movie_detail = system_object.MoviesDetail()
    movie_detail.base.Mid = movie_id
    if mysql.getMovieDetail(movie_detail) == -1:
        return 0
    _spider.movies_detail_view(movie_detail)
    mysql.close()
    return movie_detail
