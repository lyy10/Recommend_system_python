# 
#
# 系统相关接口函数
# 接口在后期根据实际情况增加删除或变动
# 目前用户总数为 943 , 用户ID 从 1-943
import sys
sys.path.append('./recommend')
import _init_users
import recommend_movies

def get_recommend_movie(user_id):
    """
        传入用户唯一ID
        程序会返回一个用户类，包含了推荐给该用户的movies电影列表
            列表中是电影类。请参照类定义
    """
    return recommend_movies.getRecommendMovies(user_id)

def isHavePicture(movie_id):
    """
        判断本地是否存在电影图片，如果不存在返回 0 请导向默认电影图片地址
        存在返回图片地址
    """

def getMovieDetail(movie_id):
    """
        获取电影详情，包括电影故事线，类别标签，跳转网址
        若没有电影详情可返回，則返回 0 ,请显示获取电影失败
        成功者返回电影详情类，请参见类设计具体信息
    """

def insertUserMovie(movie_id, user_id, Socre):
    """
        用户传回电影评分时，调用该函数保存用户数据
        传入 电影ID， 用户ID， 用户打分数（0-5)
        成功插入返回 1
        出错返回 0 ,请返回给用户错误提示
    """

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
        允许登陆返回 1
        密码或用户名错误返回 0
        没有用户返回 -1 提示用户可以注册
    """ 
    return _init_users.accessCheck(name,password)
