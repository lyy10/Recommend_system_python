#
#
# 系统爬虫
# June,6,2018 by Lyy

import requests
import re
from bs4 import BeautifulSoup
import sys
sys.path.append('./../')
sys.path.append('./../recommend/')
import system_object
import connect_db
import tqdm
from time import sleep

def movies_detail_view(movies_detail):
    print('Name: ', movies_detail.base.Name)
    print('director: ', movies_detail.director, ' creator: ', movies_detail.creator, ' stars: ', movies_detail.stars)
    print('kind: ', movies_detail.kind, ' country: ', movies_detail.country, ' language: ', movies_detail.language)
    print('story: ', movies_detail.story, ' url: ', movies_detail.url, ' runtime: ', movies_detail.runtime)
    print('post_url: ', movies_detail.base.post)
    print('local_post_url: ', movies_detail.base.local_post)

def spider(movies_detail):
    movie = movies_detail.base.Name.replace(',','')
    s = ''
    for i in movie:
        if i == '(':
            break
        s += i
    kv = {'User-Agent': 'Chromium/62.0.3202.94 Chrome/62.0.3202.94'}
    try:
        r = requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q='+s.replace(' ','+')+\
                     '&s=tt', headers = kv)
    except:
        return 0
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    #print(soup)
    data = soup.select('.findList tr .result_text')
    s_movie = movie.lower().split(' ')
    temp = ''
    for i in data:
        temp = i.a.string + i.a.next_sibling.string.rstrip()
        s_temp = temp.replace(',','').lower().split(' ')
        sign1 = True
        for item in s_movie:
            if item not in s_temp:
                sign1 = False
                break
        sign2 = True
        for item in s_temp:
            if item not in s_movie:
                sign2 = False
                break
        #print(s_movie)
        #print(s_temp)
        #print(sign1, sign2)
        if sign1 or sign2:
            movies_detail.url = 'https://www.imdb.com' + i.a['href']
            break
    if not movies_detail.url:
        return 0
    try:
        r = requests.get(movies_detail.url, headers = kv)
    except:
        return 0
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.select('#titleStoryLine')[0]
    try:
        story_temp = data.select('.inline.canwrap p span')[0].contents
        for item in story_temp:
            movies_detail.story += item.string
    except:
        pass
    movies_detail.story = movies_detail.story.strip()
    data = data.find(itemprop='genre')
    data = data.select('a')
    for a in data:
        movies_detail.kind += a.string.strip() + ','
    movies_detail.kind = movies_detail.kind[:-1]
    #print(soup.select('.poster'))
    movies_detail.base.post = soup.select('.poster')[0].img['src']
    for k in range(0,10):
        try:
            pic=requests.get(movies_detail.base.post,timeout=2)
            f=open('./../web_recommend/flask-gentelella/source/base/static/post/' + movie.replace(' ','_') + '.jpg','wb')
            f.write(pic.content)
            f.close
            movies_detail.base.local_post = '/static/post/' + movie.replace(' ','_') + '.jpg'
            break
        except:
            pass
        if k == 9:
            print('picture 异常')
    data = soup.select('.credit_summary_item')
    for i in data:
        if i.h4.string == 'Director:' or i.h4.string == 'Directors:':
            t = i.select('.itemprop')
            for j in t:
                movies_detail.director += j.string + ','
            movies_detail.director = movies_detail.director[:-1]
        elif i.h4.string == 'Writers:' or i.h4.string == 'Writer:':
            t = i.select('.itemprop')
            for j in t:
                movies_detail.creator += j.string + ','
            movies_detail.creator = movies_detail.creator[:-1]
        elif i.h4.string == 'Stars:' or i.h4.string == 'Star:':
            t = i.select('.itemprop')
            for j in t:
                movies_detail.stars += j.string + ','
            movies_detail.stars = movies_detail.stars[:-1]
    data = soup.select('#titleDetails .txt-block')
    #print(data[0].h4.string)
    for i in data:
        try:
            if i.h4.string == 'Country:':
                movies_detail.country = i.a.string
            elif i.h4.string == 'Language:':
                movies_detail.language = i.a.string
            elif i.h4.string == 'Runtime:':
                movies_detail.runtime = float(i.time.string.split()[0])
        except:
            pass
    movies_detail.base.Name = temp
    return 1
if __name__ == '__main__':
    mysql = connect_db.connect_db()
    stdout_backup = sys.stdout
    i = 175
    pbar = tqdm.tqdm(total = 1682)
    pbar.update(175)
    while(i<1683):
        #pbar.update(i)
        log_file = open("log.log", "a")
        movies_detail = system_object.MoviesDetail()
        movies_detail.base.Mid = i
        movies_detail.base.Name = mysql.getMoviesName(movies_detail.base.Mid)#'Toy Story (1995)'
        sys.stdout = log_file
        k = 0
        while k<10:
            if spider(movies_detail) != 0:
                break
            sleep(5)
            if k == 9:
                print('错误', movies_detail.base.Mid)
            k += 1
        if k == 10:
            i += 1
            pbar.update()
            log_file.close()
            continue
    #movies_detail_view(movies_detail)
        update_sql = "Title='" + movies_detail.base.Name.replace("'","\\'") + "',"
        if not movies_detail.url:
            print('异常',movies_detail.base.Mid, 'url')
        else:
            update_sql += "URL='" + movies_detail.url.replace("'","\\'") + "',"
        if not movies_detail.story:
            print('异常',movies_detail.base.Mid, 'story_line')
        else:
            update_sql += """story_line='""" + movies_detail.story.replace("'","\\'") + "',"
        if not movies_detail.kind:
            print('异常',movies_detail.base.Mid, 'kind')
        else:
            update_sql += "kind='" + movies_detail.kind.replace("'","\\'") + "',"
        if not movies_detail.base.post:
            print('异常',movies_detail.base.Mid, 'post')
        else:
            update_sql += "photo_url='" + movies_detail.base.post.replace("'","\\'") + "',"
        if not movies_detail.base.local_post:
            print('异常',movies_detail.base.Mid, 'local_post')
        else:
            update_sql += "local_photo_url='" + movies_detail.base.local_post.replace("'","\\'") + "',"
        if not movies_detail.director:
            print('异常',movies_detail.base.Mid, 'director')
        else:
            update_sql += "director='" + movies_detail.director.replace("'","\\'") +"',"
        if not movies_detail.creator:
            print('异常',movies_detail.base.Mid, 'creator')
        else:
            update_sql += "creator='" + movies_detail.creator.replace("'","\\'") + "',"
        if not movies_detail.stars:
            print('异常',movies_detail.base.Mid, 'stars')
        else:
            update_sql += "stars='" + movies_detail.stars.replace("'","\\'") + "',"
        if not movies_detail.country:
            print('异常',movies_detail.base.Mid, 'country')
        else:
            update_sql += "country='" + movies_detail.country.replace("'","\\'") + "',"
        if not movies_detail.language:
            print('异常',movies_detail.base.Mid, 'language')
        else:
            update_sql += "language='" + movies_detail.language.replace("'","\\'") + "',"
        if movies_detail.runtime == -1:
            print('异常',movies_detail.base.Mid, 'runtime')
        else:
            update_sql += "runtime=" + str(movies_detail.runtime) + ","
        #print(update_sql)
        for j in range(5):
            if mysql.updateMovie(movies_detail.base.Mid, update_sql) == -1:
                sleep(2)
            else:
                break
            if j == 4:
                print('错误', movies_detail.base.Mid, 'mysql update')
        i += 1
        sleep(1)
        sys.stdout = stdout_backup
        log_file.close()
        pbar.update()
    pbar.close()
    #log_file.close()
    mysql.close()
    print('Congratulations')
