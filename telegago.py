from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from urllib.request import urlopen, urlretrieve
from selenium.webdriver.common.keys import Keys

def main():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--log-level=3")
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    url = "https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg#gsc.tab=0"#input
    driver.get(url)
    search = input("Enter key: ")
    driver.find_element_by_xpath("/html/body/div/div[1]/div/form/table/tbody/tr/td[1]/div/table/tbody/tr/td[1]/input").send_keys(search)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr/td[2]/button").click()
    sleep(2)
    elems = driver.find_elements_by_xpath("//a[@href]")
    elemlist = []
    for elem in elems[2:-1]:
        if (elem.get_attribute("href")) not in elemlist:
            print(elem.get_attribute("href"))
            elemlist.append(elem.get_attribute("href"))
        else:
            continue

if __name__ == '__main__':
    main()
