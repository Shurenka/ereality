import time
from random import random

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, \
    ElementClickInterceptedException, JavascriptException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Logging to a console
# prepare handler
terminal = logging.StreamHandler()
# prepare formatter
terminal.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
# add handler
logger.addHandler(terminal)


def follow_people():
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                "//a[@href='/explore/people/']")))
    browser.find_element_by_xpath("//a[@href='/explore/people/']").click()
    logger.info("Opening 'explore people' page")
    # lst = browser.find_elements_by_xpath("//main/div/div[2]/div/div/div[div[2]/div/div[contains(text(), 'Подписаны')]]")
    lst = browser.find_elements_by_xpath("//*[text()='Follow']")
    logger.info(f"Created list of {len(lst)} suggested followers")
    followed = 0
    for account in lst[:10]:
        followed += 1
        time.sleep(1.2)
        #    account.find_element_by_xpath("./div[3]/button").click()
        logger.info(f"{followed} followed")
    browser.get("https://www.instagram.com/")
    logger.info("Returning to main page")


def login(code=None):
    browser.maximize_window()
    browser.get("https://www.instagram.com/")
    logger.info("Opening instagram page")
    wait = WebDriverWait(browser, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    # /html/body/div[1]/section/main/div/div/div/div/button
    if code:
        browser.find_element_by_xpath("//input[@name='username']").send_keys('+380505590159')  # '+380993660286')
        browser.find_element_by_xpath("//input[@name='password']").send_keys('webdesigner')  # '@8aua7eHSwZD')
        browser.find_element_by_xpath("//button[@type='submit']").click()
        logger.info("Entered credentials")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='verificationCode']")))
        browser.find_element_by_xpath("//input[@name='verificationCode']").send_keys(str(code))
        browser.find_element_by_xpath("//button[@type='button']").click()
        logger.info("Entered verification code")
    else:
        browser.find_element_by_xpath("//input[@name='username']").send_keys('+380993660286')
        browser.find_element_by_xpath("//input[@name='password']").send_keys('@8aua7eHSwZD')
        browser.find_element_by_xpath("//button[@type='submit']").click()
        logger.info("Entered credentials")
    try:
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
        sp = browser.find_elements_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        if sp and sp[0].text == "Не сейчас":
            sp[0].click()
            logger.info("Dismissed 'remember me' popup window")
    except TimeoutException:
        pass
    try:
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@role='presentation']/div[@role='dialog']/div/div/div[3]/button[2]")))
        browser.find_element_by_xpath(
            "//div[@role='presentation']/div[@role='dialog']/div/div/div[3]/button[2]").click()
        logger.info("Dismissed 'notification' popup window")
    except TimeoutException:
        pass


def start_liking(n):
    total = 1
    while total <= n:
        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                        "//article")))
            logger.info(f"Getting list of unliked articles")
            articles = browser.find_elements_by_xpath(
                "//section/span[1]/button[1]/div[1]//*[@aria-label='Like' or @aria-label='Нравится']")
            logger.info(f"{len(articles)} items in the list")
            if articles:
                for element in articles:
                    time.sleep(0.9)
                    element.find_element_by_xpath(
                        "//section/span[1]/button[1]/div[1]//*[@aria-label='Like' or @aria-label='Нравится']").click()
                    logger.info(f'{total} liked')
                    total += 1
                    time.sleep(1.1)
            else:
                raise NoSuchElementException
        except (StaleElementReferenceException, ElementClickInterceptedException, JavascriptException) as e:
            logger.info(e)
            browser.refresh()
        except NoSuchElementException as e:
            logger.info(e)
            try:
                while not browser.find_elements_by_xpath(
                        "//section/span[1]/button[1]/div[1]//*[@aria-label='Like' or @aria-label='Нравится']"):
                    # Scroll down to bottom
                    logger.info("Scrolling down to bottom")
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(0.8)
            except JavascriptException:
                logger.info("JavascriptException - Refreshing browser")
                browser.refresh()
                wait.until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                            "//article")))
        except Exception as e:
            logger.info(e)
            browser.refresh()


def start_liking_by_tag(tag):
    browser.get(f"https://www.instagram.com/explore/tags/{tag}/")
    try:
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//section/main/div/h2")))
        sp = browser.find_elements_by_xpath("//section/main/div/h2")
        if sp and sp[0].text == "К сожалению, эта страница недоступна.":
            logger.info("Wrong tag")
            return
    except TimeoutException:
        pass
    try:
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//header/div[2]/div[1]/div[2]/span[1]")))
        n = int(browser.find_element_by_xpath("//header/div[2]/div[1]/div[2]/span/span")
                .get_attribute('innerHTML').replace(" ", ""))

    except Exception:
        n = 1
    total = 0
    liked = 0
    logger.info(f"{n} items in the list")

    try:
        browser.find_element_by_xpath("//article/div/div/div/div/div/a/div").click()
    except Exception:
        return

    while total < n:
        try:
            total += 1
            wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//article[@role='presentation']//section//button//"
                           "*[@aria-label='Comment' or @aria-label='Комментировать']")))
            logger.info(f"Checking if {total}/{n} post is not liked yet")
            like = browser.find_elements_by_xpath(
                "//article[@role='presentation']//section//button//*[@aria-label='Like' or @aria-label='Нравится']")
            if like:
                time.sleep(random())
                like[0].click()
                liked += 1
                logger.info(f"+1 like")
                time.sleep(random())
            next_arrow = browser.find_elements_by_xpath("//a[contains(@class, 'coreSpriteRightPaginationArrow')]")
            if next_arrow:
                time.sleep(random())
                next_arrow[0].click()
                time.sleep(random())
        except Exception as e:
            browser.get(f"https://www.instagram.com/explore/tags/{tag}/")
            wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, "//header/div[2]/div[1]/div[2]/span[1]")))
            logger.info(e)
            if total > 8:
                row = (total - 9) // 3 + 1
                column = total % 3 + 1
                logger.info(f"Finding [{row}, {column}] post")
                last_height = browser.execute_script("return document.body.scrollHeight")
                while not browser.find_elements_by_xpath(f"//article/div[2]/div/div[{row}]/div[{column}]/a/div"):
                    # Scroll down to bottom
                    logger.info("Scrolling down to bottom")
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(0.8)
                    new_height = browser.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                post = browser.find_elements_by_xpath(f"//article/div[2]/div/div[{row}]/div[{column}]/a/div")
                if post:
                    post[0].click()
                else:
                    break
            else:
                row = total // 3 + 1
                column = total % 3 + 1
                browser.find_element_by_xpath(f"//article/div/div/div/div[{row}]/div[{column}]/a/div").click()
    logger.info(f"Total liked {liked} posts out of {total} viewed. Total: {n}")
    with open("result.txt", 'a') as f:
        f.write(f"For tag '{tag}' total liked {liked} posts out of {total} viewed. Total: {n}\n")


browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)

login(31498706)
# follow_people()
while True:
    tag = input("Input tag for liking\n")
    if tag == 'stop':
        break
    try:
        start_liking_by_tag(tag)
    except Exception:
        pass

browser.quit()
