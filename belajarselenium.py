import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/"

        options = webdriver.ChromeOptions()

        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.browser = webdriver.Chrome(
            service= ChromeService(ChromeDriverManager().install()), 
            options=options
        )
 
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi username
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)
    
    def test_a_failed_login_with_empty_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi username
        driver.find_element(By.ID,"password").send_keys("") # blank password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Password is required', response_data)

    def test_a_failed_login_with_empty_username_and_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("") # blank username
        driver.find_element(By.ID,"password").send_keys("") # blank password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username is required', response_data)

    def test_a_failed_login_with_incorrect_username(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_users") # incorrect username
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def test_a_failed_login_with_incorrect_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #  username
        driver.find_element(By.ID,"password").send_keys("secret_sauces") # incorrect password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def test_a_failed_login_with_incorrect_username_and_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_users") #  incorrect username
        driver.find_element(By.ID,"password").send_keys("secret_sauces") # incorrect password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()