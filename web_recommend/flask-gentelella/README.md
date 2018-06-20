<<<<<<< HEAD
[![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=master)](https://travis-ci.org/afourmy/flask-gentelella)
[![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=master)](https://coveralls.io/github/afourmy/flask-gentelella?branch=develop)

# Flask Gentelella

[Gentelella](https://github.com/puikinsh/gentelella) is a free to use Bootstrap admin template.

![Gentelella Bootstrap Admin Template](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/gentelella-admin-template-preview.jpg "Gentelella Theme Browser Preview")

This project integrates Gentelella with Flask using: 
- [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for scalability.
- [flask_login](https://flask-login.readthedocs.io/en/latest/) to implement a real login system.
- [flask_migrate](https://flask-migrate.readthedocs.io/en/latest/).

Flask-gentelella also comes with a robust CI/CD pipeline using:
- The [Pytest](https://docs.pytest.org/en/latest/) framework for the test suite (see the `tests` folder).
- [Travis CI](https://travis-ci.org/afourmy/flask-gentelella)
- [Coverage](https://coveralls.io/github/afourmy/flask-gentelella) to measure the code coverage of the tests.
- [Selenium](https://www.seleniumhq.org/) to test the application with headless chromium.
- A Dockerfile showing how to containerize the application with gunicorn, and a [Docker image](https://hub.docker.com/r/afourmy/flask-gentelella/) available on dockerhub, and integrated to the CI/CD pipeline (see instructions below).

Here is an example of a real project implemented using Flask-Gentelella:
- [Online demo](http://afourmy.pythonanywhere.com/)
- [Source code](https://github.com/afourmy/eNMS)

This project shows:
- how back-end and front-end can interact responsively with AJAX requests.
- how to implement a graph model with SQLAlchemy and use [D3.js](http://afourmy.pythonanywhere.com/views/logical_view) for graph visualization.
- how to use [Leaflet.js](http://afourmy.pythonanywhere.com/views/geographical_view) for GIS programming.
- how to use [Flask APScheduler](https://github.com/viniciuschiele/flask-apscheduler) to implement crontab-like features.

# Installation

### (Optional) Set up a [virtual environment](https://docs.python.org/3/library/venv.html) 

### 1. Get the code
    git clone https://github.com/afourmy/flask-gentelella.git
    cd flask-gentelella

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Run the code
    cd source
    python app.py

### 4. Go the http://127.0.0.1:5000/

### 5. Create an account and log in

# Run Flask Gentelella in a docker container in one command

### 1. Fetch the image on dockerhub
    docker run -d -p 5000:5000 --name gentelella --restart always afourmy/flask-gentelella

### 2. Go the http://127.0.0.1:5000/

### 3. Create an account and log in
=======
# 开发文档

interface.py 里面定义了接口函数，前端所有需要的以及要更改的数据请从这里开始,需要另外的功能请自行在这里添加，并详细说明。

system_object.py 里定了数据结构的组成形式

src 文件夹为存储用户头像，电影画报的图片等

spider 存放爬虫

web文件将全部放在web_recommend文件夹中。

# 任务分配
Lyy 的程序将在recommend文件夹里


Ch 的程序将在Recommend_system_python 根目录下，如若需要请自行建立文件夹，并把文件夹的作用在这里注明。


# 爬虫上线
>>>>>>> 095aa67d27b90fcca3472220c515a880977e3d90
