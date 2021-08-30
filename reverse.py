from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
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
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get("https://osint.sh/")
    print("Reverse Lookup")
    n=int(input("1.REVERSE IP LOOKUP 2.REVERSE WHOIS 3.REVERSE DOMAIN 4.REVERSE NAME SERVER : "))
    if(n==1):
        driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[4]/div/a").click()
        rip=input("Perform a reverse IP lookup to find all A records associated with an IP address, Enter IP : ")
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/input").send_keys(rip)
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/button").click()
        print(driver.find_element_by_xpath("/html/body/div[2]/section[3]/div/table").text)
        driver.find_element_by_xpath("/html/body/div[1]/div/nav/div/div/div[1]/div/a").click()
    elif(n==2):
        driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[12]/div/a").click()
        rwho=input("Allow you to find domain names owned by an email address, enter Email : ")
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/input").send_keys(rwho)#776eea440a28fd24220a6aa6a7fbd50f@domaindiscreet.com
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/button").click()
        try:
            print(driver.find_element_by_xpath("/html/body/div[2]/section[3]/div/table").text)
            driver.find_element_by_xpath("/html/body/div[1]/div/nav/div/div/div[1]/div/a").click()
        except:
            print("Please enter a valid email")
    elif(n==3):
        driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[13]/div/a").click()
        rk=input("Allow you to find domain names by a keyword, enter Keyword : ")
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/input").send_keys(rk)
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/button").click()
        print(driver.find_element_by_xpath("/html/body/div[2]/section[3]/div/table").text)
        driver.find_element_by_xpath("/html/body/div[1]/div/nav/div/div/div[1]/div/a").click()
    elif(n==4):
        driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[20]/div/a").click()
        rns=input("Reveal all domains that use the same name server, enter name of name server : ")
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/input").send_keys(rns)
        driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/form/button").click()
        print(driver.find_element_by_xpath("/html/body/div[2]/section[3]/div/table").text)
    
if __name__ == '__main__':
    main()