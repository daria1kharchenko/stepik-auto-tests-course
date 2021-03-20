from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('num1')
    x = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    y = int(num2.text)
    sum = str(x + y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
