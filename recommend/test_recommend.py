#
#
# 测试推荐性能参数
# May,30,2018 by Lyy
import sys
import connect_db
import recommend_movies
def test_recommend(user_id):
    mysql = connect_db.connect_db()
    recommend = recommend_movies.comput_recommend(user_id)
    test_movies = mysql.getTestMovies(user_id)
    mysql.close()
    test = []
    stdout_backup = sys.stdout
    num = len(test_movies)
    N = 0
    NN = 0
    for row in recommend:
        if int(row[0]) > 0:
            test.append([int(row[0]),row[1],0])
    #print(test)
    for i in range(len(test)):
        for row in test_movies:
            if row[0] == test[i][0]:
                test[i][2] = row[1]
                N += 1
                if row[1] >= 3:
                    NN += 1
                break
    #for row in test:
    #    print(row)
    log_file = open("log.log", "a")
    sys.stdout = log_file
    if N == 0:
        print(user_id, N/num, 0)
    else:
        print(user_id, N/num, NN/N)
    sys.stdout = stdout_backup
    log_file.close()

def test_score(user_id):
    mysql = connect_db.connect_db()
    recommend = recommend_movies.comput_recommend(user_id)
    test_movies = mysql.getTestMovies(user_id)
    have_watch = mysql.getUserMovies(user_id)
    test = []
    stdout_backup = sys.stdout
    num = len(test_movies)
    log_file = open(str(user_id) + "_recommend", "a")
    sys.stdout = log_file
    for row in recommend:
        i = 1
        for r in have_watch:
            if int(row[0]) < 0 or int(row[0]) == r.Mid:
                i = 0
                break
        if i:
            test.append([int(row[0]),row[1],0,0])
    similarity_users = mysql.getSimiUsers(user_id, 0.3)
    for i in range(len(test)):
        sign = 1
        for row in test_movies:
            if row[0] == test[i][0]:
                test[i][2] = row[1]
                sign = 0
                break
        #print(sign)
        average = []
        for j in similarity_users:
            if sign == 0:
                break
            temp = mysql.getUserMovieScore(j, test[i][0])
            #print(test[i][0],j)
            #print(temp)
            if temp != -1:
                average.append(temp)
        if sign:
            average = float(sum(average))/len(average)
            test[i][3] = average
        print(test[i][0], test[i][1], test[i][2], test[i][3])
    sys.stdout = stdout_backup
    log_file.close()
    mysql.close()

if __name__ == '__main__':
    #for i in range(1,101):
    #    print(i)
        #test_recommend(i)
    #    if i%20 == 1:
    test_score(14)
