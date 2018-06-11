# class Config(object):
#     SECRET_KEY = 'you-will-never-guess'
#     这里登录的用户名：recommend，密码：recommend，数据库地址172.16.124.17，端口3306，数据库recommend
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://recommend:recommend@172.16.124.17:3306/recommend'
#     SQLALCHEMY_TRACK_MODIFICATIONS = True


# class ProductionConfig(Config):
#     DEBUG = False


# class DebugConfig(Config):
#   DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
