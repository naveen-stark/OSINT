from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from password_generator import PasswordGenerator
import names
import os

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')


    while(1):
        gender = input("Enter gender (M/F): ")
        if (gender == 'M') or (gender == 'm'):
            break
        elif (gender == 'F') or (gender == 'f'):
            break
        else:
            continue

    name = names.get_full_name(gender)

    first_name = name.split(" ")[0]
    sur_name = name.split(" ")[1]

    pwo = PasswordGenerator()
    pwo.minlen = 8
    password = str(pwo.generate())
    print("Twitter Sock puppet creation\n")

    email = input("Please enter email: ")
    year = input("Enter year: ")
    day = input("Enter day: ")
    month = input("Enter month: ")
    print("Sock puppet creation instantiated...\nPlease wait...")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://twitter.com/i/flow/signup")
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input").send_keys(first_name + " " + sur_name)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[1]/select").send_keys(month)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[2]/select").send_keys(day)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[3]/select").send_keys(year)
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]").click()
    code = str(input("Enter security code: "))
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input").send_keys(code)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()
    sleep(5)
    print("Done! Your new id is: ", email, "and new password is: ", password)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + "\Sock account details.txt", "a")
    f.write(f"Twitter - Name: {name}, Birthday: {day}, {month}, {year}, Email: {email}, password: {password}" )
    f.close()

if __name__ == "__main__":
    main()