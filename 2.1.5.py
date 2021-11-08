from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
# Открыть страницу http://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
#Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)


#Отметить checkbox "I'm the robot".
    input2 = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    input2.click()
#Выбрать radiobutton "Robots rule!".
    input3 = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    input3.click()

# Нажать на кнопку Submit.
    button = browser.find_element_by_xpath('//button [contains(text(), "Submit")]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
