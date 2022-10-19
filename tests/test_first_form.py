import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import time


from configuration import SERVICE_URL, OSAGO_URL

from src.enums.global_enums import GlobalErrorMessages

driver = webdriver.Chrome(executable_path="D:\QA\Тестовые задания\pampadu\instrument\chromedriver.exe")

def test_valid_rissian_number():
    #проверяем доступность формы
    response = requests.get(url=OSAGO_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    #открытие формы
    driver.get(url=OSAGO_URL)
    time.sleep(2)

    #вводим гос.номер
    gos_input_main = driver.find_element_by_class_name("gos-input-main")
    gos_input_main.send_keys("А111АА")
    time.sleep(2)

    #вводим регион
    gos_input_region = driver.find_element_by_class_name("gos-input-region")
    gos_input_region.send_keys("716")
    time.sleep(2)

    #не получается найти элемент по классу, поэтому xpath. Нажимаем "Продолжить"
    continue_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/button').click()
    time.sleep(8)

    #Проверяем, что мы действительно на следующем экране формы
    assert 'Укажите марку' in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value
    assert 'Выберите модель' in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value

    driver.close()
    driver.quit()
    time.sleep(5)

def test_without_number():
    #проверяем доступность формы
    response = requests.get(url=OSAGO_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    #открытие формы
    driver.get(url=OSAGO_URL)
    time.sleep(2)

    #переходим по ссылке "Не помню или еще не получал". Опять по xpath приходится(((
    gos_link_without_number = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/span[3]').click()
    time.sleep(2)

    # Проверяем, что мы действительно на следующем экране формы
    assert 'Укажите марку' in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value
    assert 'Выберите модель' in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value

    driver.close()
    driver.quit()

def test_first_screen_form_elements():
    #проверяем доступность формы
    response = requests.get(url=OSAGO_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    #открытие формы
    driver.get(url=OSAGO_URL)
    time.sleep(2)

    #тут наверно лучше сравнивать GUI со скриншотом. Смотрим элементы интерфейса
    assert 'Калькулятор ОСАГО' in driver.page_source, GlobalErrorMessages.NO_ELEMENT.value
    assert 'Простой способ выгодно купить полис' in driver.page_source, GlobalErrorMessages.NO_ELEMENT.value
    assert 'Введите гос. номер' in driver.page_source, GlobalErrorMessages.NO_ELEMENT.value
    assert 'и мы найдем данные автомобиля' in driver.page_source, GlobalErrorMessages.NO_ELEMENT.value
    gos_input_main = driver.find_element_by_class_name("gos-input-main")
    continue_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/button')
    gos_link_without_number = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/span[3]')
    #и так далее, думаю можно найти подход лучше

    driver.close()
    driver.quit()

def test_empty_number_field():
    # проверяем доступность формы
    response = requests.get(url=OSAGO_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    # открытие формы
    driver.get(url=OSAGO_URL)
    time.sleep(2)

    continue_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/button').click()
    time.sleep(3)

    #проверяем, что не выполнен переход на следующий экран (костыль)
    assert 'Укажите марку' not in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value
    assert 'Выберите модель' not in driver.page_source, GlobalErrorMessages.WRONG_ELEMENT_NEXT_PAGE.value

    driver.close()
    driver.quit()

    #нужно разобраться почему, если запускать тесты скоупом, то выполняется только первый...

