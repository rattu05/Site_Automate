import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='travname']").send_keys("Ratnesh")
driver.find_element(By.XPATH, "//*[@id='travlastname']").send_keys("Dwivedi")

# Date Of Berth Picker
date ="5"
driver.find_element(By.XPATH, "//*[@id='dob']").click()
count = Select(driver.find_element(By.XPATH ,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
count.select_by_visible_text("Sep")
count1 = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
count1.select_by_visible_text("1998")
D = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for i in D:
    if i.text == date:
        i.click()
driver.find_element(By.XPATH, "//*[@id='sex_1']").click()
driver.find_element(By.XPATH, "//*[@id='fromcity']").send_keys("Bhopal")
driver.find_element(By.XPATH, "//*[@id='tocity']").send_keys("Katni")
# Date of Journey Picker
driver.find_element(By.XPATH, '//*[@id="departon"]').click()
date2 = "2"
count3 = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
count3.select_by_visible_text("Aug")
count4 = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
count4.select_by_visible_text("2024")
D2 = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
for i in D2:
    if i.text == date2:
        i.click()

driver.find_element(By.XPATH, '//*[@id="deliverymethod_1"]').click()
driver.find_element(By.XPATH, '//*[@id="billing_phone"]').send_keys("8770051733")
driver.find_element(By.XPATH, '//*[@id="billing_email"]').send_keys("rattu05@rd.com")

cont = Select(driver.find_element(By.XPATH, '//*[@id="billing_country"]'))
cont.select_by_visible_text("India")
driver.find_element(By.XPATH, '//*[@id="billing_address_1"]').send_keys("B-5 Venunad")
driver.find_element(By.XPATH, '//*[@id="billing_address_2"]').send_keys("Near JayAmbe Nagar")
driver.find_element(By.XPATH, '//*[@id="billing_city"]').send_keys("Ahmedabad")
count5= Select(driver.find_element(By.XPATH, '//*[@id="billing_state"]'))
count5.select_by_visible_text("Gujarat")
driver.find_element(By.XPATH, '//*[@id="billing_postcode"]').send_keys("380054")
driver.find_element(By.XPATH, '//*[@id="place_order"]').click()
time.sleep(10)
