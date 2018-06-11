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
if __name__ == '__main__':
    for i in range(1,101):
        print(i)
        test_recommend(i)
