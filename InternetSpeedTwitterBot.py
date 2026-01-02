class AutoComplainer:
    def __init__(self):
        self.complaints = [
            "Why is my internet so slow? #InternetProblems",
            "I pay for high speed internet but it feels like dial-up! #Frustrated",
            "Can someone explain why my internet is always slow? #InternetIssues",
            "Is it too much to ask for fast internet service? #NeedBetterService",
            "And every time I try to stream, my internet decides to take a break! #StreamingProblems"
        ]
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from time import sleep
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        #Keep chrome open after script execution
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chromeOptions)

        driver.get("https://www.speedtest.net/")
        go_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]'))
            )
        go_button.click()

        #Close popups
        try:
            closeButton = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/div/div[2]/a'))
            )
            closeButton.click()
            print("Popup closed")
        except Exception as e:
            print("No popup found or could not close it:", e)
        finally:
            #Get speeds
            downloadSpeed = float(driver.find_element(By.CLASS_NAME, "download-speed").text)
            uploadSpeed = float(driver.find_element(By.CLASS_NAME, "upload-speed").text)
            driver.quit()
            return downloadSpeed, uploadSpeed


        

    def post_complaint(self, mindown, minup, down, up):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.keys import Keys
        from time import sleep
        from dotenv import load_dotenv
        import os
        import random
        load_dotenv()

        #Keep chrome open after script execution
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chromeOptions)

        driver.get("https://x.com/i/flow/login")

        # signInButton = WebDriverWait(driver, 60).until(
        emailInput = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
        )
        emailInput.send_keys(os.getenv("twitteremail"))
        # ...existing code...
        nextButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@role="button" and .//span[text()="Next"]]'))
        )
        nextButton.click()
        passwordInput = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="current-password"]'))
        )
        passwordInput.send_keys(os.getenv("twitterpassword"))
        sleep(0.5)
        signInButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]'))
        )
        signInButton.click()

        #Post the complaint
        tweetInput = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]'))
        )
        tweetInput.click()
        tweetInput.send_keys(f"I need {mindown} download and {minup} upload, yet I only got {down} megabits download and {up} upload! A drastic decrease! {random.choice(self.complaints)}")
        
        sleep(2)
        tweetInput.send_keys(Keys.CONTROL, Keys.ENTER)