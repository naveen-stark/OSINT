from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from selenium.webdriver.common.keys import Keys
import os

def scroll_down(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--log-level=3")
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    uname = "soveti3259@wedbo.net"#input
    password = "39B0X4@f%@*h"#input

    url = input("Enter url: ")#https://www.facebook.com/myrecchennai/photos/
    driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjE1MzY2ODg4LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D")
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/input").send_keys(uname)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/button").click()
    sleep(5)
    driver.get(url) 
    html = driver.find_element_by_tag_name('html')
    if driver.current_url == url:
        scroll_down(driver)
    #sleep(30)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  
    #htmldata = urlopen(driver.current_url)  
    images = soup.find_all('img') 
    count = 1
    path2 = dir_path + "\\FBimages\\"
    for item in images[1:]:
        img = item['src']
        name = item.attr
        if name == None:
            path = path2 + str(count) + ".jpg"
        else:
            path = path2 + str(name) + ".jpg"
        urlretrieve(img, path)   
        sleep(1)
        count += 1
    print("Done")

if __name__ == '__main__':
    main()