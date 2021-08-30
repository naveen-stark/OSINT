from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from time import sleep
from bs4 import BeautifulSoup
import os
import tkinter as tk
import tkinter.filedialog as tkFileDialog
import sys
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--test-type")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-first-run")
    chromeOptions.add_argument("--no-default-browser-check")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)
    n=int(input("1.Advanced Search 2.Fact Checking : "))
    if (n==1):
        so=int(input("1.Surface web 2.Dark web and Deep Web : "))
        if (so==1):
            swo=int(input("1.Reverse Image Search 2.GHDB 3.Dorking : "))
            if(swo==1):
                root = tk.Tk()
                root.withdraw()    
                def browsefunc():
                    filename =tkFileDialog.askopenfilename(filetypes=(('image files', ('.png', '.jpg', '.jpeg')), ("All files","*.*")))
                    return filename
                imagename = browsefunc()
                driver.get("https://yandex.com/images/")
                driver.find_element_by_xpath("/html/body/header/div/div[2]/div[1]/form/div[1]/span/span/div[2]/button").click()
                driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/form[1]/input").send_keys(imagename)
                sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.find_all("div", {"class": "other-sites__snippet-title"})
                print("Search results: ")
                for ele in links:
                    print(ele.text)
            elif(swo==2):
                sys.tracebacklimit = 0
                exdbi=input("Enter to find Exploit : ")
                driver.get("https://www.exploit-db.com/")
                sleep(3)
                driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/label/input").send_keys(exdbi)
                sleep(8)
                print(driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div").text)
                driver.quit()
            elif(swo==3):
                f = open(dir_path + "\dorks.txt", "r",encoding="utf-8")
                print(f.read())
                advs=input("Enter dork query : ")
                driver.get("https://www.google.com/")
                driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(advs)
                driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
                sleep(2)
                alinks = []
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                results = driver.find_elements_by_css_selector('div.g')
                for ele in results:
                    link = ele.find_element_by_tag_name("a")
                    href = link.get_attribute("href")
                    alinks.append(href)
                
                hlinks = soup.find_all('h3')
                hlinks = hlinks[:-1]
                for i in range(len(hlinks)):
                    print(hlinks[i].text, "\n", alinks[i])
        elif (so==2):
            driver.get("https://ahmia.fi/")
            asi=input("Enter : ")
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[1]").send_keys(asi)
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[2]").click()
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all("li", {"class": "result"})
            a = []
            b = []
            print("Search results: ")
            for ele in links:
                for src in ele.find_all("a"):
                    a.append(src.text.strip())              
            for ele in links:
                for src in ele.find_all("cite"):
                    b.append(src.text)
            for i in range(len(a)):
                print(a[i])
                print("Tor URL: ", b[i])
                print("\n")

    elif (n==2):
        company=input("Enter News to Check Fact : ")
        first="https://hoaxy.osome.iu.edu/#query="
        sec="&sort=relevant&type=Hoaxy&lang="
        last=first+quote(company)+sec   
        driver.get(last)
        sleep(120)
        driver.find_element_by_xpath("/html/body/div[3]/section[4]/div[2]/div[6]/button").click()
        sleep(5)

if __name__ == '__main__':
    main()
        
