from selenium import webdriver
import selenium.webdriver.common.keys
import time

driver=webdriver.Chrome(executable_path='C:\Python39\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')

driver.get("https://beneficienttest.appiancloud.com/suite/")
username=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[1]/div/input")
print(username.is_displayed()) #returns true/false based element status
print(username.is_enabled()) #return true/false
username.send_keys("neeraj.kumar")

time.sleep(5)
password=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[2]/div/input")
print(password.is_displayed()) #returns true/false based element status
print(password.is_enabled()) #return true/false
password.send_keys("Crochet@786")

driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[4]/div/div[2]/input").click()
time.sleep(20)
driver.close() #close the browser
