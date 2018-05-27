# 
#
# 系统相关接口函数
# 接口在后期根据实际情况增加删除或变动
sys.path.append('./recommend')


def get_recommend_movie(user_id):
    """
        传入用户唯一ID
        程序会返回一个用户类，包含了推荐给该用户的movies电影列表
            列表中是电影类。请参照类定义
    """

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


