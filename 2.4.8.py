
# Задание: ждем нужный текст на странице

# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

import math
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

# 1 - Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
# 2 - Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
# из библиотеки expected_conditions.
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), str(100)))
# 3 - Нажать на кнопку "Book"
    browser.find_element_by_xpath("//button[@id = 'book']").click()
# 4 - Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)

    browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

    browser.find_element_by_xpath('//button[@type="submit"]').click()

# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

# Cчитывать с окна алерта правильный результат и копировать его в буфер обмена

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
