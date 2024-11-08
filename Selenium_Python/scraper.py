from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver=webdriver.Chrome()
filecsv=open('Selenium_Python/file.csv','w',encoding='utf8')
csv_columns=['name','price','img','link']
writer=csv.DictWriter(filecsv,fieldnames=csv_columns)
writer.writeheader()

driver.get("https://www.scrapingcourse.com/ecommerce/") 
# /html/body/div/div/div/div[2]/main/ul/li

products = driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/main/ul/li")

for product in products:
    name = product.find_element(By.XPATH, ".//h2").text
    price = product.find_element(By.XPATH, ".//span").text
    img = product.find_element(By.XPATH, ".//img").get_attribute("src")
    link = product.find_element(By.XPATH, ".//a").get_attribute("href")
    writer.writerow({'link': link, 'img': img, 'name': name, 'price': price})

filecsv.close()
driver.close()