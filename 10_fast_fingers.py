from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time

def main():
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options = chrome_options)

    URL = "https://10fastfingers.com/typing-test/english"
    driver.get(URL)

    wait = WebDriverWait(driver, 2)

    # This code locate the input field after this element is interactable.
    input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#inputfield")))

    start_time = time.time()
    while (time.time() - start_time) < 60:
        # This code locate the word element which is we will type to the input field. 
        words = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#row1 .highlight")))

        # This code get the actual word text from inside the word element.
        span_content = words.text
        
        # This code send the actual word text to the input field.
        input_field.send_keys(span_content)

        # This code pretend like hitting space bar to confirm words.
        input_field.send_keys(Keys.SPACE)

    driver.quit

if __name__ == "__main__":
    main()