from selenium import webdriver, common
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.action_chains import ActionChains

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("test-type")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get("https://www.jimyellowpages.com/")
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/a[3]/img").click
    sleep(2)
    city=input("Enter city name : ")
    e = driver.find_element_by_link_text(city)
    href = e.get_attribute('href')
    driver.get(href)
    f=open(dir_path + r"\jim.txt","r")
    print(f.read())
    #driver.switch_to.window(driver.window_handles[0])
    shoptype=input("Enter shop/company type : ")
    for i in range(2,6):
        try:
            e = driver.find_element_by_link_text(shoptype)
            href = e.get_attribute('href')
            driver.get(href)
            break
        except common.exceptions.NoSuchElementException:
            try:
                driver.get("https://www.jimyellowpages.com/chennai/index_"+str(i)+".htm")
            except common.exceptions.NoSuchElementException:
                pass
            
    link=driver.find_elements_by_tag_name('a') 
    for ele in link[11:-11]:
        print(ele.text)
    print("\n")

    shopname = input("Enter name of the shop/company : ")

    e = driver.find_element_by_partial_link_text(shopname)
    href = e.get_attribute('href')
    driver.get(href)
    sleep(2)
   
    
    fl = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[9]/td[2]/table[2]/tbody/tr[10]/td").text
    print(fl)
    path = dir_path + '\\' +  shopname + '.png'
    driver.get_screenshot_as_file(path)
if __name__ == '__main__':
    main()