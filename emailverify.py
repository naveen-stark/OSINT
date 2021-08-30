from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from urllib.request import urlopen, urlretrieve
from selenium.webdriver.common.keys import Keys
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def main():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_user_agents()
    user_agent = user_agent_rotator.get_random_user_agent()

    chromeOptions = ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("user-agent="+str(user_agent))
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = Chrome(options=chromeOptions)
    driver.implicitly_wait(10)
    url = "https://tools.verifyemailaddress.io/"#input
    driver.get(url)
    search = input("Enter email: ")
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/input").send_keys(search)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/div[2]/button").click()
    sleep(2)
    try:
        elems = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/div/table/tbody/tr/td[2]")
        print(elems.text)
    except:
        print("Enter valid email")
if __name__ == '__main__':
    main()