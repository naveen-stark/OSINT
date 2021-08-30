from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from password_generator import PasswordGenerator
import names
import os


def main():

    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--test-type")
    #chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    #chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)

    pwo = PasswordGenerator()
    pwo.minlen = 8
    password = str(pwo.generate())
    print("Tumblr Sock puppet creation\n")

    age = input("Enter age: ")
    blog = input("Enter blog name: ")
    email = input("Enter email: ")


    driver.get("https://www.tumblr.com/register")
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(email)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    driver.find_element_by_xpath("//input[@name=\"blogName\"]").send_keys(blog)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"age\"]").send_keys(age)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/section/div/div/div[2]/div[1]/section/div/form/div/div[2]/label/div[1]/input').click()
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    print("Done! Your new id is: ", email, "and new password is: ", password)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + "\Sock account details.txt", "a")
    f.write(f"Tumblr - Age: {age} BlogName = {blog} Email: {email}, password: {password}" )
    f.close()


if __name__ == "__main__":
    main()