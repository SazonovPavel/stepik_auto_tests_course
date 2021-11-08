
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_presence_of_button(browser):
    browser.get(" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(30)
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket')))

    assert button is not None, "this is wrong selector"













# import time
#
# def test__guest_should_see_basket_button(browser):
#     browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     browser.implicitly_wait(10)
#     assert browser.find_element_by_class_name('btn-add-to-basket')
#     time.sleep(30)


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#
# locator = r'//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
# def test_add_to_cart_btn_localization(browser, lang):
#     browser.get(link)
#
#     element = WebDriverWait(browser, 35).until(EC.visibility_of_element_located((By.XPATH, locator)))
#     actual_text = element.text
#     expected = {
#         'es': 'Añadir al carrito',
#         'fr': 'Ajouter au panier',
#         'ru': 'Добавить в корзину'}
#
#     time.sleep(3)
#     assert actual_text == expected[lang]





# import time
#
#
# def test_find_the_button(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
#     browser.get(link)
#     time.sleep(30)
#     button = browser.find_elements_by_css_selector(".btn-add-to-basket")
#
#     assert len(button) == 1, '!!! Error !!!'




