from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Name="Papa" #Name of the Receiver CapsSensitive
string="Good Morning Papa" #Message to be sent

driver=webdriver.Chrome(executable_path="C:\Prithvi\Whatsapp\chromedriver_win32 (1)\chromedriver.exe") #chrome driver path
driver.get("https://web.whatsapp.com/") #url for whatsapp
#print(driver.title)  #prints title of the page
#print(driver.current_url) #prints url of the page
while True: #keep running until break
    try:
        driver.find_element_by_xpath('//button[@class="_3e4VU"]').click() #Finding Name in order to send message 1)Clicking Search Button
        find_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]') #Finding Name in order to send message 2)Creating a message box to insaert message
        find_box.send_keys(Name) # entering receivers name
        #find_box.send_keys(Keys.ENTER) #Press Enter Key
        time.sleep(2) #Sleeps for 2s
        driver.find_element_by_xpath('//*[@title="'+Name+'"]').click() #Sending Messages 1)Entering the profile
        #text_area=driver.find_elements_by_xpath('//div[contains(text(), "' + text + '")]') 
        for i in range(5):
            message_box= driver.find_element_by_xpath('//div[@class="_3uMse"]') #Sending Messages 2)Selecting the type box
            message_box.send_keys(string) #Sending Messages 3)Writing String
            message_box= driver.find_element_by_xpath('//button[@class="_1U1xa"]') #Sending Messages 4)Finding send button and then clicking
            message_box.click()
        break

    except:
        print("Waiting For Whatsapp to open") #incase whatsapp isn,t open 
        time.sleep(5)
driver.close() #shuts off the connection
