import requests
from bs4 import BeautifulSoup

#req = requests.get('https://timesofindia.indiatimes.com/home/headlines').text
for page in range(1,9):
    weblink = f'https://www.ndtv.com/latest/page-{page}'

    req = requests.get(weblink).text

    soup = BeautifulSoup(req , 'lxml')
    #print(soup.prettify())
    try:
        for news in soup.findAll('div', class_='new_storylising_img'):

            try:
                newsimagelink = news.img['src']
                print(newsimagelink)
            #print(news.prettify())
            except:
                newsimagelink=None

            try:
                news1 = soup.find('div', class_='new_storylising_contentwrap')
                newsheading = news1.h2.a['title']
                print(newsheading)
                # newsby = news1.div.a.text
                #print(newsby)
            except:
                newsheading=None
            try:  
                newsbywithdate = news1.div.text
                print(newsbywithdate)
            except:
                newsbywithdate=None
            try:

                newsbody = news1.find('div', class_='nstory_intro').text
                print(newsbody)
                print()
            except:
                newsbody=None
                print()
    except:
        news=None
      