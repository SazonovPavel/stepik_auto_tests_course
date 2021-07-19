import os
from selenium import webdriver
import time

try:
    # 1-Открыть страницу http://suninjuly.github.io/file_input.html.
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2-Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_xpath("//input[@name='firstname']").send_keys("Pavel")
    browser.find_element_by_xpath("//input[@name='lastname']").send_keys("Sazonov")
    browser.find_element_by_xpath("//input[@name='email']").send_keys("pavel@mail.ua")

    # 3-Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)

    # 4-Нажать кнопку "Submit"
    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

