from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.CLASS_NAME, 'form-control')
    web_element.send_keys("Funcionamiento correcto!")

    driver.save_screenshot('Screenshots/imagen1.png')

    time.sleep(5)


def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.ID, "textarea")
    web_element.send_keys("Realizando pruebas con selenium webdriver")

    driver.save_screenshot('Screenshots/imagen2.png')

    time.sleep(5)


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.ID, "male")

    checkbox = driver.find_element(By.NAME, "gender")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)

    print("seleccionado antes del click: ", checkbox.is_selected())
    time.sleep(2)

    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(5)

    print("tipo de elemento:", checkbox.get_attribute('type'))
    print("seleccionado despues del click: ", checkbox.is_selected())

    driver.save_screenshot('Screenshots/imagen3.png')

    time.sleep(5)


def test_calendario():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    calendario = driver.find_element(By.ID, "datepicker")
    driver.execute_script("arguments[0].scrollIntoView();", calendario)
    calendario.click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text() = '1']").click()
    time.sleep(2)
    calendario.click()
    driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text() = '24']").click()
    time.sleep(4)

    calendario.clear()
    calendario.send_keys('12/01/2023')
    time.sleep(5)

    driver.save_screenshot('Screenshots/imagen4.png')


def test_navegacion_browser():
    driver = webdriver.Chrome()

    driver.get("https://www.mlb.com/es")
    print("url actual: ", driver.current_url)

    driver.find_element(By.XPATH, '//*[@id="react-header"]/div/header/div/div/div[2]/div[1]/nav[1]/ul/li[2]/div[1]/a').click()
    print("url actual: ", driver.current_url)

    driver.back()
    print("url actual: ", driver.current_url)

    driver.forward()
    print("url actual: ", driver.current_url)

    driver.refresh()
    print("url actual: ", driver.current_url)

    driver.save_screenshot('Screenshots/imagen5.png')

    time.sleep(5)
