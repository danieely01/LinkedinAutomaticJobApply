from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os


class LinkedIn:
    def __init__(self):
        self.path = os.environ['PATH']
        self.s = Service(self.path)
        self.PASSWORD = os.environ['PASSWORD']
        self.MAIL = os.environ['MAIL']
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.s, options=self.options)
        self.URL = "https://www.linkedin.com/jobs/search/?currentJobId=3412300846&f_AL=true&geoId=100288700&keywords=junior%20python%20developer&location=Hungary&refresh=true"

    def ApplyJob(self):
        self.driver.get(url=self.URL)
        try:
            sign_in = self.driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
            sign_in.click()
        except:
            pass
        time.sleep(3)
        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self.MAIL)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.PASSWORD)
        sign_in_button = self.driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
        sign_in_button.click()
        time.sleep(4)

        time.sleep(4)
        search_result = self.driver.find_element(By.XPATH, "//*[@id='main']/div/section[1]/div")
        scroll_cor = 100
        for n in range(30):
            self.driver.execute_script(f"arguments[0].scrollTo(0, {scroll_cor})", search_result)
            scroll_cor += 100
            time.sleep(0.5)

        job_list = self.driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")
        try:
            for job in job_list:
                job.click()
                save = self.driver.find_element(By.CLASS_NAME, "jobs-save-button")
                time.sleep(1)
                if save.text[0:5] != "Saved":
                    save.click()
                self.driver.execute_script(f"arguments[0].scrollTo(0, {scroll_cor})", search_result)
                scroll_cor += 100
                time.sleep(0.5)
                time.sleep(1)
        except NoSuchElementException:
            pass


LinkedinBot = LinkedIn()
LinkedinBot.ApplyJob()
