from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1-Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2-Нажать на кнопку
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    # 3-Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # 4-На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)

    browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

    browser.find_element_by_xpath('//button[@type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
