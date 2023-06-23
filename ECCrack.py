import chromedriver_autoinstaller
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import time as t

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

driver=[]

class ECCrack:
    def __init__(self) -> None:
        driverpath="Driver\\"+str(chromedriver_autoinstaller.get_chrome_version()).split(".")[0]+"\\chromedriver.exe"
        chromedriver_autoinstaller.install(True,"Driver\\")
        driverpath=str(chromedriver_autoinstaller.get_chrome_version()).split(".")[0]+"\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        global driver
        options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=driverpath, options=options)

        
    def CheckByString(self,stringa):
        global driver
        correctedString=str(stringa).replace(" ","+")
        correctedString=correctedString.lower()
        driver.get(f"https://www.skidrowreloaded.com/?s={correctedString}&x=0&y=0")
        Response=driver.find_element(By.XPATH,"//*[@id=\"main-content\"]/div[2]")
        if(Response.text!="No search results found, try searching again"):
            elem=driver.find_elements(By.TAG_NAME,"h2")
            stringToReturn="Result:"+elem[0].text+"\n"

            for item in elem:
                if len(correctedString)>3:
                    if str(item.text).lower().startswith(str(correctedString[0])):
                        stringToReturn+=str(item.text)+"\n"
                else:
                    stringToReturn+=str(item.text)+"\n"
                    
                
                
            return stringToReturn
                
            pass
        else:
            return "NotFound"
    def GetTorrentOfGame(self,string):
        correctedString=str(string).replace(" ","+")
        correctedString=correctedString.lower()
        driver.get(f"https://www.skidrowreloaded.com/?s={correctedString}&x=0&y=0")
        Response=driver.find_element(By.XPATH,"//*[@id=\"main-content\"]/div[2]")
        if(Response.text!="No search results found, try searching again"):
            elem=driver.find_elements(By.TAG_NAME,"h2")
            driver.get(str(elem[1].find_element(By.TAG_NAME,"a").get_attribute("href")))
            stringtoback=""
            body=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/div[5]")
            ahrefs= body.find_elements(By.TAG_NAME,"a")

            achecked=[]
            for ad in ahrefs:
                if(ad.get_attribute("rel")=="noopener" and ad.text!=""):
                    achecked.append(ad)
            
            t1=achecked[len(achecked)-1]
            if(not str(t1.text).startswith("Uploading")):
                stringtoback+="Torrent "+t1.text+":\n"+t1.get_attribute("href")+"\n"
            t1=achecked[len(achecked)-2]
            if(not str(t1.text).startswith("Uploading")):
                stringtoback+="Torrent "+t1.text+":\n"+t1.get_attribute("href")+"\n"
            
            t1=achecked[len(achecked)-3]
            if(not str(t1.text).startswith("Uploading")):
                stringtoback+="Torrent "+t1.text+":\n"+t1.get_attribute("href")+"\n"
            
            return stringtoback
            pass
        else:
            return "Game not found"

        
    
print(bcolors.WARNING+"ECCrack 1.0v")
cracktest=ECCrack()
exitbool=True;
while exitbool:
    target=""
    try:
        target=str(input("Game Name:"))
    except:
        target="Sons of the forest"
        exitbool=False

    print(cracktest.CheckByString(target))
    print("Links:\n"+cracktest.GetTorrentOfGame(target))
