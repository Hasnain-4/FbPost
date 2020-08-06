from django.shortcuts import render
from newsapi import NewsApiClient



def topnews(request):
    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news, the-verge')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist = zip(hdline, desc, img, date,ur)

#Other News..............................................

    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='News24')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist1 = zip(hdline, desc, img, date,ur)


    return render(request, 'news.html', context={"mylist":mylist,"mylist1":mylist1})



# def bbc(request):
#     newsapi = NewsApiClient(api_key="YOUR API KEY")
#     topheadlines = newsapi.get_top_headlines(sources='bbc-news')


#     articles = topheadlines['articles']

#     desc = []
#     hdline = []
#     img = []

#     for i in range(len(articles)):
#         myarticles = articles[i]

#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])


#     mylist = zip(news, desc, img)


#     return render(request, 'bbc.html', context={"mylist":mylist})