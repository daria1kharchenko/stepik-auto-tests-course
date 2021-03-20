from selenium import webdriver
import time
import os
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))
    button = browser.find_element_by_id('book')
    button.click()
    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('input_value')
    x = int(num1.text)
    res = calc(x)
    textarea = browser.find_element_by_id('answer')
    textarea.send_keys(res)
    # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
