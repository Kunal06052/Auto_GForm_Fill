from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\KUNAL VERMA\projects\chromedriver-win64\chromedriver.exe"


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get("https://forms.gle/WT68aV5UnPajeoSc8") #assignment form link



time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Kunal Verma")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("9557275418")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("atr.kunal@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("Taimoor Nagar, New Friends Colony, New Delhi, Delhi, India")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("110065")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys("05-06-2000")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Male")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("GNFPYC")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click() 
time.sleep(2) # Submit button
driver.save_screenshot('confirmation_screenshot.png')
time.sleep(2)
driver.quit()