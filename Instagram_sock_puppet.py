from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from password_generator import PasswordGenerator
import names

import os

def main():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")
    #chrome_options.add_argument('--headless')

    gender = input("Enter gender (M/F): ")
    if gender == 'M' or gender == 'm':
        gender = 'male'
    else:
        gender = 'female'

    name = names.get_full_name(gender)

    first_name = name.split(" ")[0]
    sur_name = name.split(" ")[1]

    pwo = PasswordGenerator()
    pwo.minlen = 6
    password = str(pwo.generate())

    email = input("Please enter email: ")
    year = input("Enter year: ")
    day = input("Enter day: ")
    month = input("Enter month: ")

    username = "Its" + name.replace(" ", "") + year

    print("Instagram Sock puppet creation\n")
    #r"C:\Users\nisha\Desktop\OSINT\msedgedriver.exe"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/div/label/input").send_keys(first_name + " " + sur_name)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[3]/div/label/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/label/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[6]/div/label/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").send_keys(month)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").send_keys(day)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").send_keys(year)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button").click()
    code = input("Enter code sent to your email: ")
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input").send_keys(code)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button").click()
    sleep(10)
    print("Done! Your new id is: ", email, "and new password is: ", password)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + "\\Sock account details.txt", "a")
    f.write(f"Instagram - Name: {name}, Birthday: {day}, {month}, {year}, Email: {email}, password: {password}" )
    f.close()

if __name__ == "__main__":
    main()