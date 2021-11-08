
from selenium import webdriver
import time
import math
import pyperclip
# Terminal > pip install pyperclip

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

    # Cчитывать с окна алерта правильный результат и копировать его в буфер обмена

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

# Вставить правильный результат в нужное место

    link2 = "https://www.google.com/"
    browser2 = webdriver.Chrome()
    browser2.get(link2)
    answer = pyperclip.paste()
    browser2.find_element_by_xpath('//input[@name="q"]').send_keys(answer)



    # answer = browser.find_element_by_xpath('//input[@name="q"]')
    # pyperclip.paste(answer)

    # answer = browser.find_element_by_xpath('//input[@name="q"]').pyperclip.paste

    time.sleep(5)
# >>> pyperclip.copy('The text to be copied to the clipboard.')
# >>> pyperclip.paste()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
