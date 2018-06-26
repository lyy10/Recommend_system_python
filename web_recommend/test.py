import sys
sys.path.append('./../../Recommend_system_python/')
# sys.path.append('./../recommend/')
import interface

print(interface.accessCheck('1', '1'))
print(type(interface.accessCheck('1', '1')))

user = interface.get_recommend_movie(21)
movie_id_list = []
for each in user.movies:
    movie_id_list.append(each.Mid)

watched_movie = interface.getUserHaveWatch(2)
watched_movie_id_list = []
for each in user.movies:
    watched_movie_id_list.append(each.Mid)
print(len(watched_movie_id_list))
print(len(movie_id_list))