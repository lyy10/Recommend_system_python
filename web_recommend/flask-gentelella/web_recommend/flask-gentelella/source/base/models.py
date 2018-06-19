# from flask_login import UserMixin
# from sqlalchemy import Column, Integer, String
# from database import Base
#
#
# class User(Base, UserMixin):
#
#     __tablename__ = 'User'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String(120), unique=True)
#     email = Column(String(120), unique=True)
#     password = Column(String(30))
#
#     def __init__(self, **kwargs):
#         for property, value in kwargs.items():
#             # depending on whether value is an iterable or not, we must
#             # unpack it's value (when **kwargs is request.form, some values
#             # will be a 1-element list)
#             if hasattr(value, '__iter__') and not isinstance(value, str):
#                 # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
#                 value = value[0]
#             setattr(self, property, value)
#
#     def __repr__(self):
#         return str(self.username)


from werkzeug.security import check_password_hash

# class User():
#     def __init__(self, username):
#         self.username = username
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.username


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

    def is_authenticated(self):
        return False

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
