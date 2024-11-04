from bs4 import BeautifulSoup

with open('/home/shtlp_0103/Practice_Python/bs4_python/templates/page1.html','r') as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content ,'lxml')
    tags=soup.find_all('div' , class_='card')
    for t in tags:
        print(t.h5.text)
        print(t.a.text.split()[-1])