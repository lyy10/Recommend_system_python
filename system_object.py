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
        # 海报外网地址
        self.post = ''
        # 海报本地地址
        self.local_post = ''
        # 上映日期
        self.release_data = ''

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
        self.base = Movies()

        # 以下是我所需要的，有重复的你进行合并
        # 导演
        self.director = ''
        # 编剧
        self.creator = ''
        # 主演
        self.stars = ''
        # 类型       （相当于你定义的电影类别）
        # 电影类别
        self.kind = ''
        # 制片国家/地区
        self.country = ''
        # 语言
        self.language = ''
        # 片长 以分钟为单位 -1 为未获取到
        self.runtime = -1
        # 评分 (为电影的评价评分，见电影基本类)
        # 剧情简介    （相当于你定义的电影故事线）# 电影故事线
        self.story = ''
        # 电影播放链接 （相当于你定义的电影跳转链接）# 电影跳转链接
        self.url = ''
