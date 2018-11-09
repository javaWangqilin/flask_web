from flask import Flask
import urllib
import bs4
app = Flask(__name__)

# 爬取百度新闻
def get_news():
    url = 'http://news.baidu.com/finance'
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    data = urllib.request.urlopen(req).read()
    soup = bs4.BeautifulSoup(data, 'html.parser')
    news = soup.select('#body > div a[href]')
    newsURL = ""
    title=""
    for i in range(len(news)):
        URL = news[i].get("href")
        if URL.endswith('.shtml'):
            newsURL = URL
            title = news[i].text
            break
    response = urllib.request.Request(newsURL)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    datanews = urllib.request.urlopen(response).read()
    soupnews = bs4.BeautifulSoup(datanews, 'html.parser',fromEncoding="gb18030")
    conts = soupnews.select('.left_zw')
    if len(conts)==0:
        conts=soupnews.select('article p')
    contents = ''
    images = []
    for i in range(len(conts)):
        content = conts[i]
        texts = content.text
        if texts == '':
            image = content.img
            images.append(image)
        contents = contents + texts
    return contents, title, newsURL

@app.route('/')
def hello_world():
    contents, title, newsURL=get_news()
    return contents

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)



