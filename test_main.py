from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time


def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('')

    web_element = driver.find_element(By.CLASS_NAME, '')
    web_element.click()

    time.sleep(10)


def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.ID, "")
    web_element.send_keys("")

    # driver.find_element(By.ID, "").send_keys("")

    time.sleep(10)


def test_element_by_name():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.NAME, "")
    web_element.send_keys("")

    # driver.find_element(By.NAME, "").send_keys("")

    time.sleep(10)


def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.XPATH, "")
    web_element.send_keys("")

    # driver.find_element(By.XPATH, "").send_keys("")

    time.sleep(10)


def test_textbox():
    driver = webdriver.Chrome()
    driver.get("")

    web_element = driver.find_element(By.ID, "")
    driver.switch_to.frame(web_element)

    textbox = driver.find_element(By.NAME, "")
    textbox.send_keys("")
    time.sleep(2)
    textbox.clear()
    time.sleep(2)
    textbox.send_keys("")
    time.sleep(2)
    actual_value = textbox.get_attribute('value')
    print(actual_value)

    # driver.find_element(By.XPATH, "").send_keys("")

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

    # checkbox.click()
    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(5)

    print("tipo de elemento:", checkbox.get_attribute('type'))
    print("seleccionado despues del click: ", checkbox.is_selected())


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


def test_combox():
    driver = webdriver.Chrome()
    driver.get("")

    select_file = Select(driver.find_element(By.NAME, ''))
    select_file.select_by_value('0')
    time.sleep(4)

    select_file.select_by_visible_text('')
    time.sleep(4)




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

    time.sleep(5)


def test_alert_browser():
    driver = webdriver.Chrome()

    driver.get("")

    driver.find_element(By.XPATH, "").click()

    alert = Alert(driver)
    texto = alert.text
    print("texto alerta: ", texto)

    alert.accept()

    assert driver.find_element(By.ID, "").text == "you pressed Ok!"

    time.sleep(6)


def test_cookies_browser():
    driver = webdriver.Chrome()

    driver.get("")

    print("cookies: ", driver.get_cookies())

    driver.add_cookie({"name": "Programacion 3", "value": "cookies browser"})

    print("cookies: ", driver.get_cookies())

    driver.delete_cookie("Programacion 3")
    driver.delete_all_cookies()

    print("cookies: ", driver.get_cookies())

    time.sleep(5)


def test_element_in_iframe():
    driver = webdriver.Chrome()
    driver.get("")

    my_iframe = driver.find_element(By.ID, "")
    driver.switch_to_frame(my_iframe)
    web_element = driver.find_element(By.ID, "")
    web_element.send_keys("")

    time.sleep(5)


def test_window_screen():
    driver = webdriver.Chrome()
    driver.get("")

    driver.save_screenshot('./imagen1.png')


