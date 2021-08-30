from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from selenium.webdriver.common.keys import Keys

def main():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    print("\nReddit OSINT Search\n")
    url = "https://redditcommentsearch.com/"#input
    driver.get(url)
    user_key = input("Enter username: ")
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div[1]/div[2]/input").send_keys(user_key)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div[2]/div[1]/button").click()
    sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")  
    htmldata = urlopen(driver.current_url)  
    links = soup.find_all('a') 
    lset = set()
    for ele in links:
        lset.add(ele)
    ldict = {}
    for ele in lset:
        ldict[ele.text] = (ele.get('href'))
    for key, value in ldict.items() :
        print ("\nPost: ", key,"\n", "\nLink: ", value)

if __name__ == '__main__':
    main()
