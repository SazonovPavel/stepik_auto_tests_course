from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select


try:

# 1-Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)
# 2-Посчитать сумму заданных чисел
    a = browser.find_element_by_xpath("//span[@id='num1']").text
    b = browser.find_element_by_xpath("//span[@id='num2']").text
    c = str(int(a)+int(b))

# 3-Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)
# 4-Нажать кнопку "Submit"
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла