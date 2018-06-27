<h1>说明文档</h1>

**本文档主要用于说明系统的配置等相关问题**

这里仅介绍在linux环境下安装配置该系统的流程.

<h4>1.安装虚拟环境</h4>

1.1首先在系统环境中安装虚拟环境
```
$ pip install virtualenv
```
1.2为项目创建一个虚拟环境:

这里首先在本地建了个文件夹, 例如Recommend_system
```
$ cd Recommend_system
$ virtualenv venv  #venv为虚拟环境的目录名, 目录名自定义
```
1.2激活虚拟环境

```
$ source venv/bin/activate
```
此时, 使用pip安装的包都将放在venv的文件夹中, 与全局安装的python隔绝开.

1.3 停用虚拟环境

```
$ . venv/bin/deactivate
```
<h4>2.获取代码</h4>

```
$ cd Recommend_system
$ git clone https://github.com/lyy10/Recommend_system_python.git
```

<h4>3.安装需要用到的包</h4>
```
$ cd Recommend_system_python/web_recommend/flask-gentelella
$ pip install -r requirements
```
<h4>4.运行代码</h4>
```
$ cd source
$ python app.py
```
<h4>5.在浏览器中访问:http://127.0.0.1:5000/</h4>
即可在本地将该项目运行起来.