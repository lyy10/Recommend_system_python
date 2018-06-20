import sys
sys.path.append('./../../Recommend_system_python/')
# sys.path.append('./../recommend/')
import interface

print(interface.accessCheck('1', '1'))
print(type(interface.accessCheck('1', '1')))

user = interface.getUserHaveWatch(21)
movie_id_list = []
for each in user.movies:
    movie_id_list.append(each.Mid)

print(len(movie_id_list))