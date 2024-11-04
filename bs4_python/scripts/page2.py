from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

    req_skills = "Python"

    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):    
        company_name=job.find('h3', class_="joblist-comp-name").text.strip()
        skills=soup.find('div',class_="more-skills-sections")
        skill=skills.find_all('span')
        skills = [i.text.strip() for i in skill]  # Collect skills with stripped whitespace
        url = job.find('h2', class_="heading-trun").a['href']  # Find the job URL

        with open(f'/home/shtlp_0103/Practice_Python/bs4_python/posts/{index}.txt', 'w') as f: 
            published_date = job.find('span', class_="sim-posted").span.text  
            if 'few' in published_date:  
                f.write(company_name + "\n") 
                f.write(url + "\n")  
                f.write(",".join(skills))



if __name__=='__main__':
    while True:
        find_jobs()
        time.sleep(600)
