from flask import Flask, render_template
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="3c1dc6073") # this is just a sample api key to get your own api key vist newsapi.org
    topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")
 
 
    articles = topheadlines['articles']
 
    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news,desc,img,url)
 
    return render_template('index.html', context = mylist)

@app.route('/Sports')
def sports():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    top_headlines = newsapi.get_top_headlines(country= 'in', category='sports')
    
    articles = top_headlines['articles']

    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
    return render_template('Sports.html', context = mylist)

@app.route('/Health')
def health():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    top_headlines = newsapi.get_top_headlines(category='health')
    
    articles = top_headlines['articles']

    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
    return render_template('Health.html', context = mylist)

@app.route('/Business')
def business():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    top_headlines = newsapi.get_top_headlines(category='business')
    
    articles = top_headlines['articles']

    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
    return render_template('Business.html', context = mylist)

@app.route('/Science')
def science():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    top_headlines = newsapi.get_top_headlines(category='science')
    
    articles = top_headlines['articles']

    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
    return render_template('Science.html', context = mylist)

@app.route('/Technology')
def technology():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    top_headlines = newsapi.get_top_headlines(category='technology')
    
    articles = top_headlines['articles']

    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
    return render_template('Technology.html', context = mylist)


@app.route('/index')
def index():
    newsapi = NewsApiClient(api_key="3c1dc6073964421984cc0533496eafa0")
    topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")
 
 
    articles = topheadlines['articles']
 
    desc =[]
    news = []
    img =[]
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)
 
    return render_template('index.html', context = mylist)

@app.route('/corona')
def corona():
    d =[]
    mylist = zip(d)
    return render_template('corona.html', context = mylist)
 
if __name__ == "__main__":
    app.run(debug=True)
