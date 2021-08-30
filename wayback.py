#https://web.archive.org/web/2020*/reddit.com
from selenium import webdriver
from time import sleep
def main():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)
    url = 'https://web.archive.org/web/'
    year=input("Enter Year : ")
    webname=input("Enter Website Name : ")
    hope=url+year+"*"+"/"+webname
    print(hope)
    driver.get(hope)
    sleep(10)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[3]")
    element.screenshot(webname+'.png')
    print("Past webchanges timeline has been saved as .png file")
if __name__ == "__main__":
    main()