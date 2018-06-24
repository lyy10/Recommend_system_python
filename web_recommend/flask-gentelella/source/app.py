# from config import DebugConfig
p = '/media/lyy/Data/workspace/Recommend_system_python/'
pp = [p, p+'recommend', p+'web_recommend', p+'spider']
from flask import Flask
# from flask_migrate import Migrate
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os.path import abspath, dirname, join, pardir
import sys
# sys.path.append('./../../../../Recommend_system_python/')
sys.path.extend(pp)
import interface
from system_object import User,Movies,MoviesDetail

# print(interface.accessCheck('66', '66'))
# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_source = dirname(abspath(__file__))
path_parent = abspath(join(path_source, pardir))
if path_source not in sys.path:
    sys.path.append(path_source)

# from database import db, create_database
from base.routes import login_manager
# from base.models import User

def register_extensions(app):
    # db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('home', 'base'):
        module = import_module('{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_login_manager(app, User):
    @login_manager.user_loader
    def user_loader(ID):
        print("---------------user_loader-----------------------")
        print("id:", ID)
        user = interface.get_recommend_movie(ID)
        if not user:
            return None
        user_obj = User(ID)
        user_obj.name = user.name
        return user_obj
        # return db.session.query(User).filter_by(id=id).first()

    @login_manager.request_loader
    def request_loader(request):
        print("*************request_loader**************")
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        # user = db.session.query(User).filter_by(username=username).first()
        user_id = interface.accessCheck(username, password)
        user = interface.get_recommend_movie(user_id)

        return user if user else None


# def configure_database(app):
#     create_database()
#     Migrate(app, db)
#
#     @app.teardown_request
#     def shutdown_session(exception=None):
#         db.session.remove()


def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())


# def create_app(selenium=False):
#     app = Flask(__name__, static_folder='base/static')
#     app.config.from_object(DebugConfig)
#     if selenium:
#         app.config['LOGIN_DISABLED'] = True
#     register_extensions(app)
#     register_blueprints(app)
#     from base.models import User
#     configure_login_manager(app, User)
#     configure_database(app)
#     configure_logs(app)
#     return app


# app = create_app()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, threaded=True)

app = Flask(__name__, static_folder='base/static')
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False
register_extensions(app)
register_blueprints(app)
configure_login_manager(app, User)
configure_logs(app)
app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
