from time import sleep
import requests
from bs4 import BeautifulSoup 
day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")
date = year + "-" + month + "-" + day
url = "http://www.redditarchive.com/" + date + ".html"#input
#url = "http://www.redditarchive.com/2021-03-09.html"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
llist = []
for link in soup.find_all('a'):
    if (link.get('href') == None) or ("Comments" in link.text) or ("Reddit" in link.text) or ("New Window" in link.text):
        continue
    else:
        llist.append(link.text)        
for ele in llist:
    print(ele)

