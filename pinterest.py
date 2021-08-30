from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from password_generator import PasswordGenerator
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import os

def main():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_user_agents()
    user_agent = user_agent_rotator.get_random_user_agent()
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-agent="+str(user_agent))
    print("Pinterest Sock puppet creation\n")

    pwo = PasswordGenerator()
    pwo.minlen = 8
    password = str(pwo.generate())

    age = input("Please enter age: ")

    email = input("Please enter email: ")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://in.pinterest.com/")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[3]/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[1]/fieldset/span/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[4]/fieldset/span/input").send_keys(age)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[5]/button").click()
    print("Done!, Email: ", email, "Password: ", password)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + "\Sock account details.txt", "a")
    f.write(f"Age: {age}, Email: {email}, password: {password}\n" )
    f.close()

if __name__ == "__main__":
    main()