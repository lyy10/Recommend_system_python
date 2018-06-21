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
    user = interface.get_recommend_movie(int(current_user.ID))
    movie_id_list = []
    movie_name_list = []
    movie_average_score_list = []
    movie_post_list = []
    for each in user.movies:
        movie_id_list.append(each.Mid)
        movie_name_list.append(each.Name)
        movie_average_score_list.append(round(each.average_score, 2))
        movie_post_list.append(each.post)
    count = len(movie_id_list)
    count = count//5
    return render_template('recommend.html', movie_id_list=movie_id_list, movie_name_list=movie_name_list, movie_average_score_list=movie_average_score_list, movie_post_list=movie_post_list, count=100)


@blueprint.route('/movie_details/<movie_id>')
@login_required
def movie_details(movie_id):
    movie = interface.getMovieDetail(movie_id)
    movie_id = movie_id
    movie_name = movie.base.Name
    movie_post = movie.base.post
    movie_director = movie.director
    movie_creator = movie.creator
    movie_stars = movie.stars
    movie_kind = movie.kind
    movie_country = movie.country
    movie_language = movie.language
    movie_runtime = movie.runtime
    movie_score = round(movie.base.average_score, 2)
    movie_story = movie.story
    movie_url = movie.url
    return render_template('movie_details.html', movie_id=movie_id, movie_name=movie_name,movie_director=movie_director,movie_creator=movie_creator,
                           movie_stars=movie_stars,movie_kind=movie_kind,movie_country=movie_country,movie_language=movie_language,
                           movie_runtime=movie_runtime,movie_score=movie_score,movie_story=movie_story,movie_url=movie_url,movie_post=movie_post)


@blueprint.route('/score', methods=['POST'])
@login_required
def score():
    data = json.loads(request.form.get('data'))
    print("Movie Score:", data["score"])
    return "ok"


@blueprint.route('/watched_movies')
@login_required
def watched_movies():
    user = interface.getUserHaveWatch(int(current_user.ID))
    movie_id_list = []
    movie_name_list = []
    movie_average_score_list = []
    movie_post_list = []
    for each in user.movies:
        movie_id_list.append(each.Mid)
        movie_name_list.append(each.Name)
        movie_average_score_list.append(round(each.average_score, 2))
        movie_post_list.append(each.post)
    count = len(movie_id_list)
    count = count // 5
    return render_template('watched_movies.html', movie_id_list=movie_id_list,movie_post_list=movie_post_list,movie_name_list=movie_name_list,
                           movie_average_score_list=movie_average_score_list,count=count)