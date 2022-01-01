import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import config
import time
from playsound import playsound
import requests

os.environ['PATH'] += r"C:\Users\hp\Desktop\A\CS\Selenium_dev"
driver = webdriver.Chrome()
driver.get("https://ugra.ug.edu.gh/resapply/")

driver.implicitly_wait(20)
while True:
    def Login(studID, pin):
        student_id = driver.find_element(By.ID,'studentid')
        password = driver.find_element(By.ID,'pin')

        student_id.send_keys(str(studID))
        password.send_keys(str(pin))

        loginbtn = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        loginbtn.click()

    #Substitute the parameters 'studentID' and 'pin' with your student ID and pin below
    #Example
    #Login(1234567, 01234)
    Login(studentID, pin)

    defaultTxt = "Please note : Multiple Logins not allowed"
    multipleLoginsTxt = driver.find_element(By.CSS_SELECTOR,'h3[style="text-align: center;color:red"]').text

    #Check whether portal has been opened or not
    if defaultTxt != multipleLoginsTxt:
        #executes if portal has been opened
        
        print("The portal has been opened")
        #driver.get(whatsapp)

        #music plays when this block is executed
        playsound("Legacy.mp3")
        break
        
        
    else:
        #executes if portal has not been opened
        #refreshes every 10 seconds
        print("Portal hasn't been opened yet. Kindly sit back and relax!")
        print("Refreshing....\n")
        time.sleep(10)
        driver.refresh()
        


