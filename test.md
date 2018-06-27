# 测试文档
测试人：Lyy<br>
测试时间: June 26, 2018 7:29 PM<br>
测试平台： Linux Mint 18.2<br>
测试浏览器： Chrome<br>
测试内容： 程序测试，算法推荐测试
## 推荐程序测试
项目部署在阿里云服务器，1核，1M带宽。
* test 用户登陆并成功推荐界面<br>
![推荐界面](./source/image/推荐.png)<br><br>
* 1号用户登陆成功推荐界面<br>
![1号推荐界面](./source/image/1号推荐界面.png)<br><br>
* 100号用户登陆成功推荐界面<br>
![100号推荐界面](./source/image/100号用户推荐.png)<br><br>
* 500号用户登陆成功推荐界面<br>
![500号推荐界面](./source/image/500号用户推荐.png)<br><br>
* 900号用户登陆成功推荐界面<br>
![900号推荐界面](./source/image/900号用户推荐.png)<br><br>
对比每个用户的推荐结果，我们可以看到，两两用户的被推荐的电影是不同的，并且推荐的电影的平均评分大都在3分以上。这也充分说明了我们的算法的有效性。
## 推荐效果测试
该项目使用movielens中ml-100k数据集中的ｕ1数据集，则对应有u1测试集，其中我们使用查全率和查准率来评测推荐的效果。我们使用测试程序获取了前100个用户的查全和查准率，我们只列出20个作为大致参考。
> 测试程序
> ```python
> # 测试推荐性能参数
># May,30,2018 by Lyy
>import sys
>import connect_db
>import recommend_movies
>def test_recommend(user_id):
>    mysql = connect_db.connect_db()
>    recommend = recommend_movies.comput_recommend(user_id)
>    test_movies = mysql.getTestMovies(user_id)
>    mysql.close()
>    test = []
>    stdout_backup = sys.stdout
>    num = len(test_movies)
>    N = 0
>    NN = 0
>    for row in recommend:
>        if int(row[0]) > 0:
>            test.append([int(row[0]),row[1],0])
>    #print(test)
>    for i in range(len(test)):
>        for row in test_movies:
>            if row[0] == test[i][0]:
>                test[i][2] = row[1]
>                N += 1
>                if row[1] >= 3:
>                    NN += 1
>                break
>    #for row in test:
>    #    print(row)
>    log_file = open("log.log", "a")
>    sys.stdout = log_file
>    if N == 0:
>        print(user_id, N/num, 0)
>    else:
>        print(user_id, N/num, NN/N)
>    sys.stdout = stdout_backup
>    log_file.close()
>
>```
用户ID  | 查全率 | 查准率
------------ | ------------- | --------
   1     |    1.0    |0.8102189781021898
 2 |1.0 | 0.9090909090909091
 3 | 0 | 0
 4 | 0 | 0 
 5 | 0.9880952380952381 | 0.6144578313253012
 6 | 1.0 |  0.8514851485148515 
 7 | 0.9894736842105263 | 0.9414893617021277 
 8 | 1.0 | 0.896551724137931 
 9 | 0.8 | 1.0 
 10 | 0.9888888888888889 | 1.0 
 11 | 1.0 | 0.8157894736842105 
 12 | 0.9615384615384616 | 0.96 
 13 | 0.9429657794676806 | 0.6693548387096774 
 14 |  0.9649122807017544 | 0.9090909090909091 
 15 | 1.0 | 0.5227272727272727 
 16 | 1.0 | 0.8873239436619719 
 17 | 1.0 | 0.6666666666666666 
 18 | 1.0 | 0.9830508474576272 
 19 | 0 | 0 
 20 | 1.0 | 0.6818181818181818 
表中我们可以发现，整体的查全率和查准率都处在不错的水平上，这样来看推荐效果是比较不错的，但是我们尚未考察推荐电影的排名，我们认为排名水平也是衡量推荐效果的一个指标。这里由于时间关系未进行测试。
> 注：<br>
> 由于时间关系，我们尚未来得及实现后台的维护模块。该模块表现为程序启动时的一个独立维护进程，当用户注册，对电影评分时触发该进程，对数据库进行计算和维护。因此这里暂不做测试。
