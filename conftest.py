
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ... (etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()




# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='es',
#                      help="Choose language of page")
#
# @pytest.fixture(scope='function')
# def browser(request):
#     language = request.config.getoption("language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': language})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     browser.quit()















# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default=None,
#                      help="Choose language: es, fr, ru")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     language = request.config.getoption("language")
#
#     defined_languages = {
#         "es": "es-ES",
#         "fr": "fr-FR",
#         "ru": "ru-RU"}
#     if language in defined_languages:
#         user_language = defined_languages[language]
#         options = Options()
#         options.add_argument("--log-level=3")
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#     else:
#         browser = None
#         raise pytest.UsageError("--language should be: es, fr, ru")
#
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.fixture(scope="module")
# def lang(request):
#     return request.config.getoption("language")








# import pytest
# from selenium import webdriver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--language", action="store", default=None,
#                      help="Choose language: for example: fr, en etc.")
#
# @pytest.fixture()
# def language(request):
#     language = request.config.getoption("language")
#     if language == None:
#         raise pytest.UsageError("--language should be passed")
#     return language
#
#
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()










