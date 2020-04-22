from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.firefox.FirefoxDriver;
driver = webdriver.Firefox()
driver.get('https://reportedh5.17wanxiao.com/nCovReport/index.html?token=    ') #set your token here!
wait = WebDriverWait(driver, 8)
submit = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.visible')))

submit.click()

driver.quit()
print("########################################################DONE！")
