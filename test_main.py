from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('')

    web_element = driver.find_element(By.CLASS_NAME, '')
    web_element.click()

    driver.save_screenshot('./imagen1.png')

    time.sleep(10)


def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.ID, "")
    web_element.send_keys("")

    driver.save_screenshot('./imagen2.png')

    time.sleep(10)


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.ID, "")
    driver.switch_to.frame(web_element)

    checkbox = driver.find_element(By.NAME, "")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    print("seleccionado antes del click: ", checkbox.is_selected())
    time.sleep(2)

    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(5)

    print("tipo de elemento:", checkbox.get_attribute('type'))
    print("seleccionado despues del click: ", checkbox.is_selected())

    driver.save_screenshot('./imagen3.png')

    time.sleep(5)


def test_calendario():
    driver = webdriver.Chrome()
    driver.get("")

    calendario = driver.find_element(By.ID, "")
    calendario.click()
    time.sleep(2)

    driver.find_element(By.XPATH, "").click()
    time.sleep(2)
    calendario.click()
    driver.find_element(By.XPATH, "").click()
    time.sleep(4)

    calendario.clear()
    calendario.send_keys('01/01/1000')
    time.sleep(4)

    driver.save_screenshot('./imagen4.png')


def test_navegacion_browser():
    driver = webdriver.Chrome()

    driver.get("")
    print("url actual: ", driver.current_url)

    driver.find_element(By.LINK_TEXT, "").click()
    print("url actual: ", driver.current_url)

    driver.back()
    print("url actual: ", driver.current_url)

    driver.forward()
    print("url actual: ", driver.current_url)

    driver.refresh()
    print("url actual: ", driver.current_url)

    driver.save_screenshot('./imagen5.png')

    time.sleep(5)
