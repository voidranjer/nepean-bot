from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import sys

# seed = "https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
# court_name = "Badminton"
# time_aria = "6:30 PM Friday February 17, 2023"
# telephone = '0123456789'
# email = 'test@gmail.com'
# name = 'James'

headless = True
retry_rate = 0.01

# seed = sys.argv[1]
# court_name = sys.argv[2]
# time_aria = sys.argv[3]
# telephone = sys.argv[4]
# email = sys.argv[5]
# name = sys.argv[6]
# env = sys.argv[7]


def auto_book(seed, court_name, time_aria, telephone, email, name, is_test_run):
    try:
        options = Options()
        if (headless):
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        driver.get(seed)

        court_name_xpath = f"//div[@class='content' and text()='{court_name}']"
        driver.find_element_by_xpath(court_name_xpath).click()

        while True:
            try:
                element = driver.find_element_by_xpath(
                    f"//a[@aria-label='{time_aria}']")
            except:
                print("Element not found, trying again...")
                driver.refresh()
                time.sleep(retry_rate)
                continue
            break

        driver.execute_script("arguments[0].click();", element)

        driver.find_element_by_id('telephone').send_keys(telephone)
        driver.find_element_by_id('email').send_keys(email)
        driver.find_element_by_xpath(
            "//input[starts-with(@id,'field')][@type='text']").send_keys(name)
        # driver.find_element_by_id('field5970').send_keys(name)

        driver.find_element_by_id('submit-btn').click()

        if (not is_test_run):
            driver.find_element_by_id('submit-btn').click()

        time.sleep(5)
        driver.quit()
        print(f"Successfully booked {court_name} at {time_aria} for {name}")
        return True
        # sys.stdout.flush()
    except:
        return False
