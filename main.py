import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class  yellow_cow:
    
    def __init__(self, lag = 3):
        options = webdriver.FirefoxOptions()
        # options = webdriver.ChromeOptions()
        options = webdriver.FirefoxOptions()
        # options.add_experimental_option("mobileEmulation", { "deviceName": "Nexus 5" })
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-features=DefaultPassthroughCommandDecoder")
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized') # 
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-3d-apis")
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        options = webdriver.FirefoxOptions()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        self.option = options
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\ben\\Documents\\GitHub\\Yellow_Cow\\webdriver\\geckodriver\\geckodriver.exe", options = options)
        self.lag = lag
        
    def login(self, credentials):
        driver = self.driver
        driver.get("https://www.urbtix.hk/login")
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.NAME, "loginId"))
        )
        time.sleep(self.lag)
        driver.find_element(By.NAME, "loginId").send_keys(credentials['username'])
        driver.find_element(By.NAME, "password").send_keys(credentials['passwd'])
        driver.find_element(By.CSS_SELECTOR, '.button-wrapper.login-button.blue').click()
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "home-container"))
        )
    def buy_ticket(self, link, quantity = 4):
        driver = self.driver
        ## Add 4 tickets to basket and confirm
        driver.get(link)
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.XPATH,"//div[@title='Purchase Ticket']"))
            # EC.presence_of_element_located((By.CSS_SELECTOR,".buy-icon.icon']"))
        )
        time.sleep(self.lag)
        
        while True:
            try:
                driver.find_element(By.XPATH, "//div[@title='Purchase Ticket']").click()
            except:
                continue
            else:
                break           
        # driver.find_element(By.CSS_SELECTOR, '.buy-icon.icon').click()

        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CLASS_NAME,'area-info  '))
        )
        time.sleep(self.lag)
        
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CLASS_NAME,'name'))
        )
        time.sleep(self.lag)
        
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CLASS_NAME,'price'))
        )
        time.sleep(self.lag)
        
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.button-wrapper.cart-button.blue.disabled'))
        )
        time.sleep(self.lag)
        
        while True:
            try:
                driver.find_elements(By.CLASS_NAME, 'area-info  ')[0].click()
            except:
                continue
            else:
                break            
        
        
        for i in range(quantity):
            driver.find_elements(By.CLASS_NAME, 'icon-add ')[0].click()
        
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR,'.button-wrapper.select-button.blue').click()
            except:
                continue
            else:
                break        

        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".button-wrapper.cart-button.blue"))
        )
        time.sleep(self.lag)
        
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR,'.button-wrapper.cart-button.blue').click()
            except:
                continue
            else:
                break         
        
    def check_out(self, card_details):
        driver = self.driver
        ## Check Out
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".button-wrapper.continue.blue"))
        )
        time.sleep(self.lag)
        
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR,'.button-wrapper.continue.blue').click()
            except:
                continue
            else:
                break          
        
        ## Card Details
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".input-content.field-input"))
        )
        time.sleep(self.lag)        
        
        while True:
            try:
                ## Card Type
                driver.find_element(By.XPATH,"//div[@title='MASTER CARD']").click()
                
                ## Card Number
                driver.find_element(By.NAME,"cardNumber").send_keys(card_details['card_number'])              
               
                ## Security Code
                driver.find_element(By.NAME, "cardSafeCode").send_keys(card_details['SafeCode'])
                                
            except:
                continue
            else:
                break
 
        while True:
            try:
                ## Expire Month
                print("Expire Month")
                driver.find_elements(By.CSS_SELECTOR,"span[class='input-suffix-icon']")[1].click()
                list_option = driver.find_elements(By.CLASS_NAME,"select-option  ")
                for l in list_option:
                    if l.text == card_details['MM']:
                        l.click()
                        break
            except:
                continue
            else:
                break
            
        while True:
            try:
                ## Expire Year
                print("Expire Year")
                driver.find_elements(By.CSS_SELECTOR,"span[class='input-suffix-icon']")[2].click()
                list_option = driver.find_elements(By.CLASS_NAME,"select-option  ")
                for l in list_option:
                    if l.text == card_details['YY']:
                        l.click()
                        break
            except:
                continue
            else:
                break
            
        ## Continue Button
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR,'.button-wrapper.continue.blue').click()             
            except:
                continue
            else:
                break      
               
        ## Agree Buttons
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(((By.XPATH,"//div[@title='selected']")))
        )
        time.sleep(self.lag)
        while True:
            try:
                driver.find_elements(By.XPATH,"//div[@title='selected']")[1].click()   
                driver.find_elements(By.XPATH,"//div[@title='selected']")[2].click()   
                driver.find_elements(By.CSS_SELECTOR,'.button-wrapper.confirm.blue')[1].click()
            except:
                continue
            else:
                break        

revolut = {
    "card_number" : 5354567905458617,
    "MM" : "07",
    "YY" : "2027",
    "SafeCode" : "306"
}

credentials = {
    "username" : "ikjldsa",
    "passwd" : "Ikjldsa.123"
}

## Test
test = yellow_cow(lag=0)
test.login(credentials=credentials)
test.buy_ticket(link="https://www.urbtix.hk/event-detail/9598/", quantity=2)
test.check_out(card_details = revolut)


# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")
# driver.find_elements_by_css_selector("span[class='input-suffix-icon']")

# driver.find_element_by_css_selector("span[class='input_group_button']")

# driver.find_element_by_xpath("//div[@title='Confirm']")[0].click()

# element_list = driver.find_elements_by_class_name('button-inner')

# element_list.find_element_by_xpath("//div[@tabindex='0']")

# driver.find_element(By.NAME, "Add to Cart")


# driver.find_element(By.TAG_NAME, '')

# driver.switch_to.frame(driver.find_element_by_id('root'))
# driver.set_page_load_timeout(10)
# driver.get("https://www.urbtix.hk/")

# driver.find_elements_by_class_name('main___3Egpk')
# print(driver.page_source)
# # import time
# # import selenium
# # from selenium import webdriver
# # from selenium.webdriver.chrome import Opera


# # webdriver_service = service.Service('C:\\Users\\ben\\Documents\\GitHub\\Yellow_Cow\\operadriver_win32\\operadriver.exe')


# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By

# from selenium import webdriver
# OpOption = webdriver.OperaOptions()
# option.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Opera(executable_path='C:\\Users\\ben\\Documents\GitHub\\Yellow_Cow\\operadriver_win32\\operadriver.exe')
# driver.get("https://www.urbtix.hk/")


 
# # driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get("https://dev.to")
 
# driver.find_element_by_id("nav-search").send_keys("Selenium")

