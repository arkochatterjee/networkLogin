from selenium import webdriver
import time
chromedriver = "./chromedriver.exe"  #download the chrome web driver for the automation

browser = webdriver.Chrome(chromedriver)
browser.get('https://192.168.10.3/connect/PortalMain')  #directs to the webpage
time.sleep(2)
username = browser.find_element_by_id("LoginUserPassword_auth_username")  #goes to the mentioned field
username.send_keys("Login")  #enter you login id

password = browser.find_element_by_id("LoginUserPassword_auth_password")  #goes to the mentioned field
password.send_keys("Password")  #enter your password

browser.execute_script("oAuthentication.submitActiveForm()")  #clicks the login button
