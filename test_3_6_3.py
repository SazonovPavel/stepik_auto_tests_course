import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


message_text = ""

links_sites = [
    ("236895/step/1"),
    ("236896/step/1"),
    ("236897/step/1"),
    ("236898/step/1"),
    ("236899/step/1"),
    ("236903/step/1"),
    ("236904/step/1"),
    ("236905/step/1")
]


@pytest.mark.parametrize('links_sites', links_sites)
def test_aliens_links(browser, links_sites):
    link = f"https://stepik.org/lesson/{links_sites}/"
    browser.get(link)
    # Еее, думал, больше провожусь с заданием, сильно помог комментарий про send_keys(),
    # он принимает только строки, а не числа) поэтому переводите время в строку)
    #  Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера
    # text_area = browser.find_element_by_tag_name('textarea')
    browser.find_element_by_tag_name('textarea').send_keys(str(math.log(int(time.time()))))
    # time.sleep(10)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()

    time.sleep(5)

    # 13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем переменной
    message = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

    # 14. Проверяем не равен ли он !="Correct!"
    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    # if message != "Correct!":
    #     message += message_text
    #     print(message_text)

    # assert message_text == "Correct!"
    # print(message_text)


    # time.sleep(5)
    # 15. если не равен то добавляем в переменную с 4 пункта посредством self. название переменной += с пункта 13 пунк переменная и print()
    #
    # 16. assert с пункта13  переменная == False проверяем
    #

    assert message == "Correct!", \
        f"{message}"

    # time.sleep(10)




#--------------------------------------------------

# Запустите тест:

# pytest -s -v test_fixture7.py







#
# В упавших тестах найдите кусочки послания.
# Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!"
# Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
#
# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено
# правильное локальное время (https://time.is/ru/).
# Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.


#--------------------------------------------------



# Структура
#
# 1. Фикстура browser. как в предыдущих примерах.
#
# 2. Класс который начинается на Test. Как в предыдущих примерах.
#
# 3. Внутри класса 2 переменные: 1. пустая для сообщения = "".  2. массив со списком адресов
#
# 4.Внутри класса также есть функция с parametrize('название переменной для исползования внутри этой функции= неважно какое но желательно подходящее по смыслу я назову links', "название переменой масива со списком адресов") похожее на предыдущий урок
#
# 5. Эта функция тест поэтому название функции должно начинаться на test_
#
# 6. Эта функция получает self, browser, и название переменной для исползования внутри этой функции( с 4 пункта ' ' я назову links например)
#
# Внутри функции:
#
# 7.  Первые 2 строчки как в предыдущем примере 2 предпоследние с небольшим изменением в link
#
# 8. browser.implicity_wait(10)
#
# 9. Ищем textarea
#
# 10. Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера
#
# 11. Через WebDriverWait EC.element_to_be_clickable находим класс кнопку
#
# 12. нажимаем на кнопку
#
# 13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем переменной
#
# 14. Проверяем не равен ли он !="Correct!"
#
# 15. если не равен то добавляем в переменную с 4 пункта посредством self. название переменной += с пункта 13 пунк переменная и print()
#
# 16. assert с пункта13  переменная == False проверяем
#
# 17.
#
# if __name__ == "__main__":
#
#     unittest.main()
