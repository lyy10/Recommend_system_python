# 
#
# 系统数据库相关接口函数
# 接口在后期根据实际情况增加删除或变动
# 目前用户总数为 943 , 用户ID 从 1-943
p = '/home/chenghui/project/Recommend_system/Recommend_system_python/'
pp = [p, p+'recommend', p+'web_recommend', p+'spider']
import sys
sys.path.extend(pp)

sys.path.append('./recommend')
# import _init_users
sys.path.append('./spider/')
sys.path.append('./../Recommend_system_python/')
from recommend import _init_users
from recommend import recommend_movies
import _init_movies
import _spider
def get_recommend_movie(user_id):
    """
        传入用户唯一ID
        程序会返回一个用户类，包含了推荐给该用户的movies电影列表
            列表中是电影类。请参照类定义
    """
    return recommend_movies.getRecommendMovies(user_id)

#def isHavePicture(movie_id):
    """
        函数废弃，包含于电影基本类中
        判断本地是否存在电影图片，如果不存在返回 0 请导向默认电影图片地址
        存在返回图片地址
    """

def getMovieDetail(movie_id):
    """
        获取电影详情，包括电影故事线，类别标签，跳转网址
        若没有电影详情可返回，則返回 0 ,请显示获取电影失败
        成功者返回电影详情类，请参见类设计具体信息
    """
    return _init_movies.getMovieDetail(movie_id)

def insertUserMovie(user_id, movie_id, movie_score):
    """
    切记： 在调用该函数前，一定要检查该用户是否登陆！！！！
        用户传回电影评分时，调用该函数保存用户数据
        传入 用户ID，电影ID ， 用户打分数（0-5)
        成功插入返回 1
        出错返回 -1 ,请返回给用户错误提示
    """
    return _init_movies.insertMovieScore(user_id, movie_id, movie_score)
def isHaveName(name):
    """
        用户修改用户名或注册重名检测，不允许重名，
        传入名字 字符串        
        重名返回 1
        否则返回 0
    """
    return _init_users.isHaveName(name)

def accessCheck(name, password):
    """
        用户登陆检测，检测用户及密码是否正确
        传入用户名字符串， 密码字符串
        允许登陆返回 用户ID
        密码或用户名错误返回 0
        没有用户返回 -1 提示用户可以注册
    """ 
    return _init_users.accessCheck(name,password)

def getUserHaveWatch(user_id):
    """
        获取用户看过的电影，传入用户唯一ID
        程序会返回一个用户类，包含了该用户看过的movies电影列表
    """
    return _init_movies.getUserHaveWatch(user_id)

def insertUser(user_name, user_password):
    """
        插入新用户，传入用户名及ID
        插入成功返回用户ID，失败返回 -1 为重用户名，不允许重用户名
    """

    return _init_users.insert_user(user_name, user_password)

def getUserName(user_id):
    """
        获取用户名字，成功返回用户名字符串
        失败返回 0
    """
    return _init_users.getUserName(user_id)

if __name__=='__main__':
    #_spider.movies_detail_view(getMovieDetail(1))
    #print(insertUserMovie(1,1,5))
    pass
