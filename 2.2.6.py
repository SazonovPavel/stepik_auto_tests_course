from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

# 1-Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://SunInJuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

# 2-Считать значение для переменной x.
    x_value = browser.find_element_by_xpath("//span[@id='input_value']").text

# 3-Посчитать математическую функцию от x.
    x = calc(x_value)

# 4-Проскроллить страницу вниз.
#     button = browser.find_element_by_tag_name("button")
    button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

# 5-Ввести ответ в текстовое поле.
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(x)

# 6-Выбрать checkbox "I'm the robot".
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()

# 7-Переключить radiobutton "Robots rule!".
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()

# 8-Нажать на кнопку "Submit".
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла