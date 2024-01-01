import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument('--disable-popup-blocking')
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(options=options)
# 
# path of webdriver
PATH = "E:\chromedriver-win64\chromedriver.exe"
driver.get("https://www.linkedin.com/home")
driver.maximize_window()
######
mail='takashigaming27@gmail.com'
password='1212!@!@'
driver.find_element(By.XPATH,"//input[@type='text']").send_keys(mail)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@data-id='sign-in-form__submit-btn']").click()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3720911240&geoId=103363366&location=Dhaka%2C%20Bangladesh&origin=JOBS_HOME_LOCATION_AUTOCOMPLETE&refresh=true")
time.sleep(5)
driver.quit()
