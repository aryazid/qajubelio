from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://app2.jubelio.com/")
text_box_email = driver.find_element(by=By.NAME, value="email")
text_box_password = driver.find_element(by=By.NAME, value="password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="span.ladda-label")

#Empty form
submit_button.click()
time.sleep(2)

#Invalid email and password
text_box_email.send_keys("ngasal@gmail.com")
text_box_password.send_keys("ngasal123")
submit_button.click()
time.sleep(2)

#validemail empty password
text_box_email.clear()
text_box_password.clear()
text_box_email.send_keys("aryazid10@gmail.com")
submit_button.click()
text_box_email.clear()
time.sleep(2)

#valid password empty email
text_box_email.clear()
text_box_password.send_keys("ojaoijo")
submit_button.click()
time.sleep(2)
text_box_password.clear()

#LowLenght
text_box_email.send_keys("ngas")
text_box_password.send_keys("ngas")
submit_button.click()
time.sleep(2)

#Valid email and password
text_box_email.clear()
text_box_password.clear()
text_box_email.send_keys("aryazid10@gmail.com")
text_box_password.send_keys("m3WG9S3f'/';.3@3Bi")
submit_button.click()
time.sleep(4)


alert = driver.find_element(by=By.CSS_SELECTOR, value="li")
driver.quit()