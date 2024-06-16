from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

EmailCredential = "****"
PassWordCredential = "****"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

time.sleep(2)

iAccept = driver.find_elements(By.XPATH, '//*[@id="u1584650407"]/div/div[2]/div/div/div[1]/div[1]/button')[0]
iAccept.click()

logIn = driver.find_elements(By.LINK_TEXT, 'Log in')[0]
logIn.click()

time.sleep(2)

facebookSignIn = driver.find_elements(By.XPATH, '//*[@id="u-143730669"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')[0]
facebookSignIn.click()

time.sleep(2)

facebookWindow = driver.window_handles[1]
driver.switch_to.window(facebookWindow)

time.sleep(1)

EmailInput = driver.find_elements(By.NAME, 'email')[0]
EmailInput.send_keys(EmailCredential)

PassWordInput = driver.find_elements(By.NAME, 'pass')[0]
PassWordInput.send_keys(PassWordCredential)

PassWordInput.send_keys(Keys.RETURN)
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)

allowLocation = driver.find_elements(By.XPATH, '//*[@id="u-143730669"]/div/div/div/div/div[3]/button[1]')[0]
allowLocation.click()

time.sleep(2)

dismissNotifications = driver.find_elements(By.XPATH, '//*[@id="u-143730669"]/div/div/div/div/div[3]/button[2]')[0]
dismissNotifications.click()    

counter = 0
while counter < 99:
    likeButton = driver.find_elements(By.XPATH, '//*[@id="u1584650407"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')[0]
    likeButton.click()
    time.sleep(1)
    counter+=1

driver.quit()


