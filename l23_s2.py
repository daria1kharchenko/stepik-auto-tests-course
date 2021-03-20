from selenium import webdriver
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('input_value')
    x = int(num1.text)
    res = calc(x)
    textarea = browser.find_element_by_id('answer')
    textarea.send_keys(res)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
