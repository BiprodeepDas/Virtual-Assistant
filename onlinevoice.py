from prompt_toolkit.contrib.telnet.protocol import EC
from selenium import webdriver     #for online
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import NoSuchElementException



chrome_options = Options()
path = Service(executable_path=r'D:\My Projects\Collg Project\The virtual assistant\coding\chromedriver-win64\chromedriver.exe')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('Headless= False')
driver = webdriver.Chrome(service=path,options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(20)

website=r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
Buttonselection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
Buttonselection.select_by_visible_text('British English / Brian')

def speak(Text) :
        length = len(str(Text))
        if length==0 :
            pass
        else :
            print(f"AI : {Text}")
            print(" ")
            Data = str(Text)
            xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
            driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
            driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
            driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()

            if length>=5 :
                sleep(4)

            elif length>=40 :
                sleep(6)

            elif length>=55 :
                sleep(8)

            elif length>=70 :
                sleep(10)

            elif length>=100 :
                sleep(13)

            elif length>=120 :
                sleep(14)

            else:
                sleep(2)


speak("Hii")


