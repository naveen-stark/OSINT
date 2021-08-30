from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://phonebook.cz/")
    while(True):
        ch = int(input("1. Domains\n2. Email\n3. URL's\n"))
        if ch == 1:
            search = input("Enter search term: ")
            driver.find_element_by_xpath("/html/body/section/form/input[1]").send_keys(search)
            driver.find_element_by_xpath("/html/body/section/form/input[2]").click()
            driver.find_element_by_xpath("/html/body/section/form/button").click()
            sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")  
            htmldata = urlopen(driver.current_url)  
            links = soup.find_all('a') 
            links = links[:-4]
            for ele in links:
                if ele != '#':
                    print(ele.text)
            break
        elif ch == 2:
            search = input("Enter search term: ")
            driver.find_element_by_xpath("/html/body/section/form/input[1]").send_keys(search)
            driver.find_element_by_xpath("/html/body/section/form/input[3]").click()
            driver.find_element_by_xpath("/html/body/section/form/button").click()
            sleep(3)
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")  
            htmldata = urlopen(driver.current_url)  
            links = soup.find_all('a') 
            links = links[:-4]
            for ele in links:
                if ele != '#':
                    print(ele.text)
            break
        elif ch == 3:
            search = input("Enter search term: ")
            driver.find_element_by_xpath("/html/body/section/form/input[1]").send_keys(search)
            driver.find_element_by_xpath("/html/body/section/form/input[4]").click()
            driver.find_element_by_xpath("/html/body/section/form/button").click()
            sleep(7)
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")  
            htmldata = urlopen(driver.current_url)  
            links = soup.find_all('a') 
            links = links[:-4]
            for ele in links:
                if ele != '#':
                    print(ele.text)
            break
        else:
            continue
        
if __name__ == '__main__':
    main()
