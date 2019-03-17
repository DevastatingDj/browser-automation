from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'E:/chromedriver_win32/chromedriver.exe')
driver.get("https://www.irctc.co.in/nget/train-search")

ID = 'userid'
PASS = 'password'


def login():
    elem = driver.find_element_by_link_text("LOGIN")
    elem.click()
    time.sleep(0.5)

    user_id = driver.find_element_by_id("userId")
    user_id.click()
    user_id.clear()
    user_id.send_keys(ID)

    password = driver.find_element_by_id("pwd")
    password.click()
    password.clear()
    password.send_keys(PASS)


def find(src, dest, doj):     # find("LUCKNOW NE - LJN", "NEW DELHI - NDLS", "20-10-2018")
    from_station = driver.find_element_by_xpath('//*[@id="origin"]/span/input')
    from_station.click()
    from_station.clear()
    from_station.send_keys(src)

    to_station = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
    to_station.click()
    to_station.clear()
    to_station.send_keys(dest)

    date_of_journey = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
    date_of_journey.click()

    for i in range(10):
        date_of_journey.send_keys(Keys.BACKSPACE)

    date_of_journey.send_keys(doj)  # dd-mm-yyyy

    down_arrow = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[3]/span')
    down_arrow.click()
    time.sleep(0.1)

    tier = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[7]/span')
    tier.click()

    flexible_with_date_checkbox = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[6]/div/label')
    flexible_with_date_checkbox.click()

    find_trains = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button')
    find_trains.click()


def passenger(name, age, gender, no):     # passenger("Dhananjai Sharma", 21, "m", 8130393405)
    name_field = driver.find_element_by_xpath('//*[@id="psgn-name"]')
    name_field.clear()
    name_field.send_keys(name)

    age_field = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[2]/input')
    age_field.clear()
    age_field.send_keys(age)

    gender_window = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select')
    gender_window.click()

    if gender == "m":
        gender_field = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select/option[2]')
        gender_field.click()
    elif gender == "f":
        gender_field = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select/option[3]')
        gender_field.click()

    number = driver.find_element_by_xpath('//*[@id="mobileNumber"]')
    number.clear()
    number.send_keys(no)

