from .config import MAIN_URL  # Импортируем URL из модуля pages.config
from urllib.parse import urlparse  # Импортируем функцию urlparse из модуля urllib.parse
from selenium.webdriver.support.wait import WebDriverWait  # Импортируем класс WebDriverWait из модуля selenium.webdriver.support.wait
from selenium.webdriver.support import expected_conditions as EC  # Импортируем модуль expected_conditions из selenium.webdriver.support

# Класс для работы с простой страницей
class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver  # Инициализируем драйвер
        self.base_url = MAIN_URL  # Устанавливаем базовый URL
        self.driver.implicitly_wait(timeout)  # Устанавливаем неявное ожидание драйвера

    # Переходим на сайт
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # Ищем элемент на странице с заданным локатором
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')  # Возвращаем сообщение, если элемент не найден

    # Ищем все элементы на странице с заданным локатором
    def find_many_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not find {locator}')  # Возвращаем сообщение, если элементы не найдены

    # Возвращаем относительную ссылку (путь) страницы
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    # Поиск элемента, который является кликабельным
    def find_element_until_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')  # Возвращаем сообщение, если элемент не кликабельный
