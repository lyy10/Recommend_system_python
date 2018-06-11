# related object
# May,26,2018 by Lyy
# June,11,2018 updated by Ch

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
class User():
    def __init__(self, ID):
        # 用户ID
        self.ID = ID
        # 用户名
        self.name = ''
        # 用户电影列表
        self.movies = []

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.ID

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

        # 以下是我所需要的，有重复的你进行合并
        # 导演
        # 编剧
        # 主演
        # 类型       （相当于你定义的电影类别）
        # 制片国家/地区
        # 语言
        # 上映日期
        # 片长
        # 评分
        # 剧情简介    （相当于你定义的电影故事线）
        # 电影播放链接 （相当于你定义的电影跳转链接）