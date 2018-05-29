#
# 
# May,28,2018 by Lyy

import connect_db
import system_object
import math

def maintain_similarity(user_id):
    mysql = connect_db.connect_db()
    num = 943
    #num = mysql.getNumUser()
    if num == -1:
        return -1
    main_user = mysql.getUserMovies(user_id)
    lens_main = len(main_user)
    for i in range(user_id+1,num+1):
        if i == user_id:
            continue
        temp = mysql.getUserMovies(i)
        #print(main_user)
        lens_temp = len(temp)
        k = 0
        j = 0
        same = [[],[]]
        while k < lens_main and j < lens_temp:
            if main_user[k].Mid < temp[j].Mid:
                k += 1
            elif main_user[k].Mid > temp[j].Mid:
                j += 1
            else:
                same[0].append(float(main_user[k].user_score))
                same[1].append(float(temp[j].user_score))
                k += 1
                j += 1
        if len(same[0]) == 0:
            mysql.updateSimilarity(user_id, i, -1, 0, 0, 0)
            continue
        sum1 = sum(same[0])/len(same[0])
        sum2 = sum(same[1])/len(same[1])
        sim1 = 0
        sim2 = 0
        sim3 = 0
        for k in range(0,len(same[0])):
            sim1 += (same[0][k]-sum1)*(same[1][k]-sum2)
            sim2 += (same[0][k]-sum1)**2
            sim3 += (same[1][k]-sum2)**2
        sim1 += 1
        sim2 += 1
        sim3 += 1
        just = float(len(same[0]))/20
        if just > 1:
            just = 1
        sim = float(sim1)/(math.sqrt(sim2)*math.sqrt(sim3))*just
        if mysql.updateSimilarity(user_id, i, sim, sim1, sim2, sim3) == -1:
            return -1
    mysql.close()
    return 1
num = 943
for i in range(1,num):
    if maintain_similarity(i) == -1:
        print('wrong')
        break
    print(str(i) + ': right')
#if maintain_similarity(1) == -1:
#    print('wrong')
#else:
#    print("right")
