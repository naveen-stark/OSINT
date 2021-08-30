from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import os
from pathlib import Path
import requests
from time import sleep
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup

def main():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_user_agents()
    user_agent = user_agent_rotator.get_random_user_agent()

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("user-agent="+str(user_agent))
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)
    filename = Path('metadata.pdf')
    i1=input("Enter Company name : ")
    n=int(input("1.Annual reports \n2.Company Relationship Lookup : "))
    if (n==1):
        driver.get("https://www.annualreports.com/")
        driver.find_element_by_xpath("/html/body/div/section[1]/div/form/fieldset/div[1]/input[1]").send_keys(i1)
        driver.find_element_by_xpath("/html/body/div/section[1]/div/form/fieldset/div[1]/input[2]").click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        sleep(2)
        table = soup.find("table")
        namelist = ["Fill"]
        links = table.find_all('a')
        for ele in links:
            namelist.append(ele.text)
        
        for ele in namelist[1:]:
            print(namelist.index(ele), " ", ele)
        ari=int(input("Choose the company : "))
        ari = namelist[ari]
        driver.find_element_by_link_text(ari).click()
        e = driver.find_element_by_xpath("/html/body/div/div[2]/article/div[2]/ul/li[1]/div[2]/ul/li[2]/a")
        href = e.get_attribute('href')
        driver.get(href)
        #driver.switch_to.window(driver.window_handles[1])
        #url = driver.current_url
        response = requests.get(href)
        filename.write_bytes(response.content)
        print("Info saved as .pdf format")
    elif (n==2):
        driver.get("https://littlesis.org/")
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div/div[3]/form/div/input").send_keys(i1)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div/div[3]/form/div/div/button").click()
        sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        link = soup.find_all("div", {"class": "search-result-wrapper entity-search-result"})
        alinks = []
        for ele in link:
            alinks.append(ele.find('a').text)
        alinks.insert(0, "Fill")
        if len(alinks)<2:
            print("No company found")
        else:
            for ele in alinks[1:]:
                print(alinks.index(ele), " ", ele)
            lsi=int(input("Choose the company : "))
            driver.find_element_by_link_text(alinks[lsi]).click()
            sleep(3)
            driver.find_element_by_link_text('Data').click()
            sleep(3)
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/a").click()
            sleep(5)
            print("Info saved as .csv format")

if __name__ == '__main__':
    main()
