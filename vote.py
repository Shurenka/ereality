import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from params import site, user, password

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(site)
time.sleep(0.5 + random.randint(1, 3))
login = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "loginName")))
login.send_keys(user)
time.sleep(0.5 + random.randint(1, 3))
browser.find_element_by_xpath("//*[@name='pass']")\
    .send_keys(password + Keys.ENTER)

time.sleep(3 + random.randint(1, 10))
while 1:
    el = browser.find_elements_by_xpath('//*[@id="main"]/#document')
    if el:
        print(el[0])
    else:
        print('Could not find element with such id')
    time.sleep(0.2)

# def voting():
#     menu = WebDriverWait(browser, 10).until(
#         expected_conditions.presence_of_element_located
#         ((By.XPATH, "//li[@class='InfoMenu']/a")))
#     menu.click()
#     time.sleep(3 + random.randint(1, 10))
#     prof = WebDriverWait(browser, 10).until(
#         expected_conditions.presence_of_element_located
#         ((By.ID, "globalMenuItem14")))
#     prof.click()
#     time.sleep(3 + random.randint(1, 10))
#     browser.switch_to.frame("main")
#     vote = browser.find_element_by_xpath(
#         "//a[contains(@href,'/holiday.php?click')]")
#     vote.click()
#
#
# voting()
#
# move = WebDriverWait(browser, 10).until(
#     expected_conditions.presence_of_element_located
#     ((By.XPATH, "//div[@class='TopBar_right']/a")))
# move.click()
#
# search_place = WebDriverWait(browser, 10).until(
#     expected_conditions.presence_of_element_located
#     ((By.ID, "SearchPlaceOpened]")))
# if search_place.style == "display: none;":
#     sp_menu = WebDriverWait(browser, 10).until(
#         expected_conditions.presence_of_element_located
#         ((By.XPATH, "//li[@class='SearchPlace']/a"))).click()
