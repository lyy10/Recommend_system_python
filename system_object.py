#

#related object
# May,26,2018 by Lyy
# Movies Object

class Movies(object):
    def __init__(self, _Mid=-1, _Socre=-1):
        # 电影ID
        self.Mid = _Mid
        # 在用户类中起作用，用户对电影的评分
        self.user_score = _Socre
        # 电影的平均评分
        self.averay_socre = -1
        # 电影名字
        self.Name = ''

# User object
class User(object):
    def __init__(self, ID):
        # 用户ID
        self.ID = ID
        # 用户名
        self.name = ''
        # 用户电影列表
        self.movies = []

# Movies Detail object
class MoviesDetail(object):
    def __init__(self):
        # 电影基本类
        self.movies = Movies()
        # 电影故事线
        self.story = ''
        # 电影类别
        self.kind = ''
        # 电影跳转链接
        self.url = ''
