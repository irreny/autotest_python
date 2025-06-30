"""Фикструры"""
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def browser():
    """Основная фикстура по браузеру"""
    # Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('start-maximized')  # открыть на полный экран
    chrome_options.add_argument('--disable-infobars')  # отключить инфсообщения
    chrome_options.add_argument('--disable-extensions')  # отключаем расширения
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-search-engine-choice-screen')  # отключить выбор движка для поиска
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()
