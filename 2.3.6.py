from selenium import webdriver
import time
import math
import pyperclip


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1-Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2-Нажать на кнопку
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    # 3-Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 4-Пройти капчу для робота и получить число-ответ
    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)

    browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

    browser.find_element_by_xpath('//button[@type="submit"]').click()

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
