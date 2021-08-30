from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://analyzeid.com/username/")

    search = input("Enter username: ")

    driver.find_element_by_xpath("//html/body/div[2]/main/div/div/div/div/div[1]/div/div/div/form/div[1]/input").send_keys(search)
    driver.find_element_by_xpath("/html/body/div[2]/main/div/div/div/div/div[1]/div/div/div/form/div[2]/button").click()
    sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    takentable = soup.find("table", {"id": "taken"})
    availtable = soup.find("table", {"id": "available"})
    list_of_rows1 = []
    list_of_rows2 = []
    for row in takentable.find_all('tr'):
        list_of_cells1 = []
        for cell in row.find_all(["th","td"]):
            text = cell.text
            list_of_cells1.append(text)
        list_of_rows1.append(list_of_cells1)

    for row in availtable.find_all('tr'):
        list_of_cells2 = []
        for cell in row.find_all(["th","td"]):
            text = cell.text
            list_of_cells2.append(text)
        list_of_rows2.append(list_of_cells2)

    print("Username available in: ")
    for item in list_of_rows1:
        print(item[0])

    print("Username unavailable in: ")
    for item in list_of_rows2:
        print(item[0])

if __name__ == '__main__':
    main()