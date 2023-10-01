from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://app2.jubelio.com/")
text_box_email = driver.find_element(by=By.NAME, value="email")
text_box_password = driver.find_element(by=By.NAME, value="password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="span.ladda-label")

driver.maximize_window()
#Login
text_box_email.clear()
text_box_password.clear()
text_box_email.send_keys("aryazid10@gmail.com")
text_box_password.send_keys("private")
submit_button.click()
time.sleep(7)

menu_barang = driver.find_element(by=By.CSS_SELECTOR, value="#wrapper > nav > div > div > ul > li:nth-child(2) > a")
menu_persediaan = driver.find_element(by=By.CSS_SELECTOR, value="#wrapper > nav > div > div > ul > li:nth-child(2) > ul > li:nth-child(2) > a")
menu_barang.click()
time.sleep(3)
menu_persediaan.click()
time.sleep(4)
checkbox_gjk = driver.find_element(by=By.CSS_SELECTOR, value="#page-wrapper > div.wrapper.wrapper-content > div > div > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div > div > div.react-grid-Container > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div > div.rdg-row-actions-cell.react-grid-Cell.react-grid-Cell--frozen > div > div > span > div > label")
checkbox_gjk.click()
time.sleep(2)

penyesuaian_persediaan = driver.find_element(by=By.XPATH, value='//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]/span[1]')
penyesuaian_persediaan.click()
time.sleep(6)

keterangan = driver.find_element(by=By.XPATH, value='//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/textarea')
keterangan.send_keys("Hari ini terjual 10 pcs")
time.sleep(3)

#button_plusormin = driver.find_element(by=By.XPATH, value='//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div')
#button_plusormin.click(2)
time.sleep(3)

checkbox_persediaan = driver.find_element(by=By.XPATH, value='//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[10]/div/div/span/div/label')
checkbox_persediaan.click()
time.sleep(3)

value_plusormin = driver.find_element(by=By.XPATH, value='//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]')
time.sleep(1)
display = driver.find_element(by=By.XPATH, value='//*[@id="page-top"]/div[6]/div/input')
display.send_keys("10")



time.sleep(3)

time.sleep(3)

