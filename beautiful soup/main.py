import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
#Get title of the html page 
title = soup.title
#Get all the paragraphs from the page
paras = soup.find_all('p')
#Get all the anchor tags from the page 
anchors = soup.find_all('a')
#Get first element  in the html page 
print(soup.find('p'))
# find all the elements with class lead
print(soup.find_all("p",class_="lead"))
#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())
#Get all the anchor tags from the page 
anchors = soup.find_all('a')
all_links = set()
#Get all the links in page:
for link in anchors:
    if(link.get('href')!='#'):
        linkTest = "https://www.flipkart.com" +link.get('href')
        all_links.add(link)
        print(linkTest)

