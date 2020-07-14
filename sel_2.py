from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Name="Papa"
string="Good Morning Papa"

driver=webdriver.Chrome(executable_path="C:\Prithvi\Whatsapp\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
#print(driver.title)
#print(driver.current_url)
while True:
    try:
        driver.find_element_by_xpath('//button[@class="_3e4VU"]').click()
        find_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
        find_box.send_keys(Name)
        #find_box.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@title="'+Name+'"]').click()
        #text_area=driver.find_elements_by_xpath('//div[contains(text(), "' + text + '")]')
        for i in range(5):
            message_box= driver.find_element_by_xpath('//div[@class="_3uMse"]')
            message_box.send_keys(string)
            message_box= driver.find_element_by_xpath('//button[@class="_1U1xa"]')
            message_box.click()
        break

    except:
        print("Waiting For Whatsapp to open")
        time.sleep(5)
driver.close()
