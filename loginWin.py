from selenium import webdriver
import time
chromedriver = "./chromedriver.exe"

browser = webdriver.Chrome(chromedriver)
browser.get('https://192.168.10.3/connect/PortalMain')
time.sleep(2)
username = browser.find_element_by_id("LoginUserPassword_auth_username")
username.send_keys("RA1611003010758")

password = browser.find_element_by_id("LoginUserPassword_auth_password")
password.send_keys("Cse^3980")

browser.execute_script("oAuthentication.submitActiveForm()")
