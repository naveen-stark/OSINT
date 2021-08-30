from selenium import webdriver
import urllib.request
from time import sleep
import os 
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    age = input("Enter age: ")
    gender = input("Enter 'male' or 'female': ")
    URL = "https://fakeface.rest/face/view?gender=" + gender + "&minimum_age=" + age 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    sleep(1)
    html = driver.current_url
    urllib.request.urlretrieve(html, dir_path + r"\sock_puppet.jpg")
    print("Image saved")

if __name__ == "__main__":
    main()