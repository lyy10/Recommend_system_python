#
#
# 系统爬虫
# June,6,2018 by Lyy

import requests
import re
from bs4 import BeautifulSoup

def spider(movie):
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q='+movie.replace(' ','+')+\
                     '&s=tt', headers = kv)
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    #print(soup)
    data = soup.select('.findList tr .result_text')
    src = ''
    for i in data:
        temp = i.a.string + i.a.next_sibling.string.rstrip()
        if temp == movie:
            src = i.a['href']
            break
    if src == '':
        return 0
    r = requests.get('https://www.imdb.com/title/tt0114709/?ref_=fn_tt_tt_1', headers = kv)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.select('#titleStoryLine')[0]
    story_line = data.find(itemprop='description').string.strip()
    data = data.find(itemprop='genre')
    data = data.select('a')
    kind =''
    for a in data:
        kind += a.string.strip() + ','
    kind = kind[:-1]
    photo = soup.select('.poster')[0].img['src']
    print(photo)
    pic=requests.get(photo,timeout=1)
    f=open('./../src/movies/' + movie.replace(' ','_') + '.jpg','wb')
    f.write(pic.content)
    f.close
    
    #





if __name__ == '__main__':
    spider('Toy Story (1995)')
