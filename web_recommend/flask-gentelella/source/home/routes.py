p = '/home/chenghui/project/Recommend_system/Recommend_system_python/'
pp = [p, p+'recommend', p+'web_recommend']
from flask import Blueprint, render_template, request
from flask_login import (
    current_user,
    LoginManager,
    login_required,
    login_user,
    logout_user
)
import json
import sys
sys.path.extend(pp)

import interface
from system_object import User,Movies,MoviesDetail

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='/home',
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/recommend')
@login_required
def recommend():
    user = interface.get_recommend_movie(current_user.ID)
    movie_id_list = []
    movie_name_list = []
    movie_averay_socre_list = []
    for each in user.movies:
        movie_id_list.append(each.Mid)
        movie_name_list.append(each.Name)
        movie_averay_socre_list.append(each.averay_socre)

    return render_template('recommend.html', movie_id_list=movie_id_list, movie_name_list=movie_name_list, movie_averay_socre_list=movie_averay_socre_list)


@blueprint.route('/movie_details')
@login_required
def movie_details():
    return render_template('movie_details.html')


@blueprint.route('/score', methods=['POST'])
@login_required
def score():
    data = json.loads(request.form.get('data'))
    print("Movie Score:", data["score"])
    return "ok"


@blueprint.route('/watched_movies')
@login_required
def watched_movies():
    return render_template('watched_movies.html')