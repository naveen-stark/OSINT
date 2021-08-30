from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

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
    chromeOptions.add_argument("test-type")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)

    email = input("Enter email: ")
    URL = "https://haveibeenpwned.com/"
    driver.get(URL)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/input[1]").send_keys(email)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/span/button").click()
    sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    hack = []

    for x in soup.findAll('div',attrs={"class":"pwnTitle"}):
        hack.append((x.find('p').text))
    if hack[-1] == '':
        print("\nNo data breachs found!")
    else:
        for x in soup.find_all("div", {"class":"col-sm-10"}):
            print("\n", x.find('p').text, "\n")
    
if __name__ == '__main__':
    main()
