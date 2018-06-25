#
#
# 采用图算法，计算可推荐的电影
# May,29,2018 by Lyy
import sys
sys.path.append('./../')
import system_object
import connect_db
import numpy as np
from numpy.linalg import solve
import time
from scipy.sparse.linalg import gmres,lgmres
from scipy.sparse import csr_matrix
import tqdm

def comput_recommend(user_id):
    mysql = connect_db.connect_db()
    similarity_users = mysql.getSimiUsers(user_id, 0.3)
    if similarity_users is -1:
        re = mysql.getInitMovies(-1)
        mysql.close()
        return re
    similarity_users.append(user_id)
    #print(similarity_users)
    similarity_movies = []
    user_index = {}
    movies_index = {}
    movies_sign = 0
    user_out = []
    user_movies = []
    movies_out = []
    for row in similarity_users:
        user_movies.append([])
    for i in range(len(similarity_users)):
        user_index[str(similarity_users[i])] = i
        temp = mysql.getUserMovies(similarity_users[i])
        user_out.append(len(similarity_users))
        for k in range(len(temp)):
            if str(temp[k].Mid) not in movies_index.keys():
                movies_index[str(temp[k].Mid)] = movies_sign
                movies_sign += 1
                similarity_movies.append(temp[k].Mid)
                for j in range(len(similarity_users)):
                    user_movies[j].append(0)
                user_movies[i][movies_sign-1] += 1
            else:
                user_movies[i][movies_index[str(temp[k].Mid)]] += 1
    mysql.close()
    T = np.array(user_movies).T
    #print(T.T[0])
    for row in T:
        movies_out.append(row.sum())
    lens = len(similarity_users) + len(similarity_movies)
    M = np.zeros((lens,lens))
    M[0:len(similarity_users),len(similarity_users):] = T.T.copy()
    M[len(similarity_users):,0:len(similarity_users)] = T
    for i in range(len(similarity_users)):
        M[i] = M[i]/user_out[i]
    k = 0
    for i in range(len(similarity_users),lens):
        M[i] = M[i]/movies_out[k]
        k += 1
    #for row in M:
    #    print(row)
    #print(M[len(similarity_users)-1])
    #print(M[0])
    similarity_users = [str(-e) for e in similarity_users]
    similarity_movies = [str(e) for e in similarity_movies]
    return comput_group(M.tolist(), similarity_users+similarity_movies)

def comput_group(M, vertex):
    """
        该算法函数参考网络
        https://blog.csdn.net/Mr_tyting/article/details/65638435
    """
    #print(vertex)
    alpha=0.8
    M = np.matrix(M)
    s = []
    for i in range(len(vertex)-1):
        s.append([0])
    s.append([1])
    r0=np.matrix(s)#从'b'开始游走
    #print(r0.shape)
    n=M.shape[0]
    #直接解线性方程法
    A=np.eye(n)-alpha*M.T
    b=(1-alpha)*r0
    begin=time.time()
    r=solve(A,b)
    end=time.time()
    #print('user time',end-begin)
    rank={}
    for j in range(n):
        rank[vertex[j]]=r[j]
    li=sorted(rank.items(),key=lambda x:x[1],reverse=True)
    #for ele in li:
    #    print("%s:%.3f,\t" %(ele[0],ele[1]))
    #采用CSR法对稀疏矩阵进行压缩存储，然后解线性方程
    data=list()
    row_ind=list()
    col_ind=list()
    for row in range(n):
        for col in range(n):
            if (A[row,col]!=0):
                data.append(A[row,col])
                row_ind.append(row)
                col_ind.append(col)
    AA=csr_matrix((data,(row_ind,col_ind)),shape=(n,n))
    begin=time.time()
    r=gmres(AA,b,tol=1e-08,maxiter=1)[0]
    end=time.time()
    #print("user time",end-begin)
    rank={}
    for j in range(n):
        rank[vertex[j]]=r[j]
    li=sorted(rank.items(),key=lambda x:x[1],reverse=True)
    #for ele in li:
    #    print("%s:%.3f,\t" % (ele[0], ele[1]))
    temp = []
    for ele in li:
        temp.append([ele[0],ele[1]])
    return temp
#comput_recommend(405)
def getRecommendMovies(user_id):
    movies = comput_recommend(user_id)
    mysql = connect_db.connect_db()
    have_watch = mysql.getUserMovies(user_id)
    recommend = []
    if movies is not -1:
        for row in movies:
            i = 1
            for r in have_watch:
                if int(row[0]) < 0 or int(row[0]) == r.Mid:
                    i = 0
                    break
            if i:
                recommend.append(int(row[0]))
    user = system_object.User(user_id)
    user.name = mysql.getUserName(user_id)
    for i in range(len(recommend)):
        movie = system_object.Movies(recommend[i])
        #movie.Name = mysql.getMoviesName(recommend[i])
        if mysql.getUserMovieDetail(movie) == -1:
            continue
        user.movies.append(movie)
    mysql.close()
    return user
def maintainRecommendList(user_id):
    movies = comput_recommend(user_id)
    mysql = connect_db.connect_db()
    have_watch = mysql.getUserMovies(user_id)
    recommend = []
    if movies is not -1:
        for row in movies:
            i = 1
            for r in have_watch:
                if int(row[0]) < 0 or int(row[0]) == r.Mid:
                    i = 0
                    break
            if i:
                recommend.append(int(row[0]))
    mo = ''
    for i in recommend:
        mo += str(i) + ','
    mo = mo[:-1]
    if mo is not '':
        mysql.updateInitMovies(mo, user_id)
        mysql.close()
        return 1
    mysql.close()
    return -1

def getmaintainRecommendMovies(user_id):
    mysql = connect_db.connect_db()
    re = mysql.getInitMovies(user_id)
    recommend = []
    for i in re:
        recommend.append(i[0])
    user = system_object.User(user_id)
    user.name = mysql.getUserName(user_id)
    many = len(recommend)
    if many > 100:
        many = 100
    for i in range(many):
        movie = system_object.Movies(recommend[i])
        #movie.Name = mysql.getMoviesName(recommend[i])
        if mysql.getUserMovieDetail(movie) == -1:
            continue
        user.movies.append(movie)
    mysql.close()
    return user
#user = getRecommendMovies(405)
#print(user.ID,user.name)
#for row in user.movies:
#    print(row.Mid,row.Name)
if __name__=='__main__':
    #pbar = tqdm.tqdm(range(1,945))
    #for i in pbar:
    #    if maintainRecommendList(i) == -1:
    #        print('wrong:', i)
    pass
