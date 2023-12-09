from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
import schedule
from selenium.common.exceptions import *
# driver = webdriver.Chrome()
# driver.get("https://web.snapchat.com/?ref=snapchat_dot_com_login_cta")

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")

#provide location where chrome stores profiles
options.add_argument(r"--user-data-dir=C:\Users\risha\AppData\Local\Google\Chrome\User Data")

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Default')

#specify where your chrome driver present in your pc
driver = webdriver.Chrome(options=options)

#provide website url here
driver.get("https://web.snapchat.com/")

ClicktosendSnap='/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div/button'
check_elem = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/nav/div[1]/div/div/div[2]")))
count=[0]
def sendSnap(Text=None):
        print(f"Running {count[0]}")
        wait = WebDriverWait(driver, 10)
        ClicktosendSnapButton = wait.until(lambda x: x.find_element(By.XPATH,ClicktosendSnap))
        ClicktosendSnapButton.click()
        print("Clicked to send Snap Button")

        TakeImage='/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/button[1]'
        TakeImageButton = wait.until(lambda x: x.find_element(By.XPATH,TakeImage))
        TakeImageButton.click()
        print("PHOTO TAKEN")

        if(Text!=None):
            Text=f'{Text} {count[0]}'
            count[0]+=1
            AddText='/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[2]'
            AddTextButton =wait.until(lambda x: x.find_element(By.XPATH,AddText))
            AddTextButton.click()
            actions = ActionChains(driver)
            actions.send_keys(Text)
            actions.perform()
            

        Send='/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/button[2]'
        SendButton = wait.until(lambda x: x.find_element(By.XPATH,Send))
        SendButton.click()
        print("Clicked on Send")

        # AllButton="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/form/div/div[2]/button[2]"
        
        AllButtons="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/form/div/div[2]"
        time.sleep(2)
        AllButtonsElement=wait.until(lambda x: x.find_element(By.XPATH,AllButtons))
        Sendlists=AllButtonsElement.find_elements(By.XPATH,"*")

        allSnaps="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/form/div/div[2]/button[2]"
        allSnapsButton=wait.until(lambda x: x.find_element(By.XPATH,allSnaps))
        allSnapSymbol="😀"
        # 🤐

        for i in Sendlists:
            if(i.text==allSnapSymbol):
                allSnapsButton=i

        allSnapsButton.click()
        print("all Snaps")


        PeopleList="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/form/div/ul"
        PeopleListElement=wait.until(lambda x: x.find_element(By.XPATH,PeopleList)).find_elements(By.XPATH,"*")

        for i in PeopleListElement[1:]:
            
            # if("My AI" in i.text):
            i.click()
                # print(i.text)
            # break
        print("Snaps Send")

        SendSnapsFinally="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/form/div[2]/button"
        SendSnapsFinallyButton=wait.until(lambda x: x.find_element(By.XPATH,SendSnapsFinally))
        SendSnapsFinallyButton.click()

        time.sleep(1)

        Close="/html/body/main/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/button"
        CloseButton=wait.until(lambda x: x.find_element(By.XPATH,Close))
        CloseButton.click()
        print("Back to Original State")


        
print("SNAP ITS LOADED")
# sendSnap()
schedule.every(15).hours.do(lambda :sendSnap()) 
  
while True: 
    # print("inside loop")
    schedule.run_pending() 
    time.sleep(60) 
# time.sleep(500)

    #     def tagspam(name,tag,message,n):
    # search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    # search.send_keys(name)
    # search.send_keys(Keys.RETURN)
    # textem = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    # for i in range(0,n):
    #     textem.send_keys(tag)
    #     textem.send_keys(Keys.RETURN)
    #     textem.send_keys(message)
    #     textem.send_keys(Keys.RETURN)

# check_elem = WebDriverWait(driver, 200).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")))
# tagspam("Valorant","@khu","spam incomming",100000)
