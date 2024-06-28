from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
ttt
import time
import pickle



options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def auth(link):
        driver.get(link)
        driver.implicitly_wait(10)

        for c in pickle.load(open('cookies', "rb")):
            driver.add_cookie(c)
        time.sleep(1)

        driver.refresh()
        time.sleep(10)


def get_sub():
        sub_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a")
        time.sleep(2)
            
        action.move_to_element(sub_btn).click().perform()
        time.sleep(7)
        
        el = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div/div")
        time.sleep(1)

        scroll = ScrollOrigin.from_element(el)
        leng = 500
        
        for i in range(5):
            action.scroll_from_origin(scroll, 0, leng).perform()
            time.sleep(4)
            leng+=1000
        time.sleep(3)
        
        subs = driver.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")
        time.sleep(10)
        
        with open("username.txt", "a") as f:
            for sub in subs:
                f.write(sub.text + " ")
            
    

try:   
    channel_name = ""
    def main():
        auth(f"https://www.instagram.com/{channel_name}/")
        get_sub()
        
    main()
except Exception as ex:
    print(ex)


