import os

import pytest
from dotenv import load_dotenv
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

URL = 'https://pokemonbattle-stage.ru/'

USER_LOGIN = os.getenv('USER_LOGIN')
USER_PASS = os.getenv('USER_PASS')
INCORRECT_LOGIN = os.getenv('INCORRECT_LOGIN')
INCORRECT_PASS = os.getenv('INCORRECT_PASS')


def test_positive_login(browser):
    """Позитивная проверка авторизации."""

    browser.get(URL)

    email_input = browser.find_element(
        by=By.CSS_SELECTOR, value=('[class*="k_form_f_email"]')
    )
    email_input.click()
    email_input.send_keys(USER_LOGIN)

    password_input = browser.find_element(by=By.ID, value='k_password')
    password_input.click()
    password_input.send_keys(USER_PASS)

    button = browser.find_element(
        by=By.CSS_SELECTOR, value=('[class*="k_form_send_auth"]')
    )
    button.click()  # Нажать кнопку "Войти"

    WebDriverWait(
        browser,
        timeout=15,
        poll_frequency=7
    ).until(EC.url_to_be(URL))

    trainer_id = browser.find_element(
        by=By.CSS_SELECTOR,
        value='[class="header_card_trainer_id_num"]'
    )

    assert trainer_id.text == '2993', 'Неожиданный trainer id'


CASES = [
    ('1', INCORRECT_LOGIN, USER_PASS, ['Введите корректную почту']),
    ('2', USER_LOGIN, INCORRECT_PASS, ['Неверные логин или пароль']),
    ('3', INCORRECT_LOGIN, USER_PASS, ['Введите корректную почту']),
    ('4', '', USER_LOGIN, ['Введите почту']),
    ('5', USER_LOGIN, '', ['Введите пароль']),
]


@pytest.mark.parametrize('case_number, email, password, alerts', CASES)
def test_negative_login(case_number, email, password, alerts, browser):
    """Негативная проверка авторизации."""

    logger.info(f'Case : {case_number}')
    browser.get(URL)

    email_input = browser.find_element(
        by=By.CSS_SELECTOR, value=('[class*="k_form_f_email"]')
    )
    email_input.click()
    email_input.send_keys(email)  # Ввод логина

    password_input = browser.find_element(by=By.ID, value='k_password')
    password_input.click()
    password_input.send_keys(password)  # Ввод пароля

    button = browser.find_element(
        by=By.CSS_SELECTOR, value=('[class*="k_form_send_auth"]')
    )
    button.click()  # Нажать кнопку "Войти"

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(  # Ожидаем ответ от бэка
        EC.visibility_of_any_elements_located(
            (By.CSS_SELECTOR, '[class*="auth__error"]')
        )
    )

    alerts_messages = browser.find_elements(
        by=By.CSS_SELECTOR,
        value=('[class*="MuiFormHelperText-root"]')
        )

    alerts_list = []
    for element in alerts_messages:
        alerts_list.append(element.text)

    assert alerts_list == alerts, 'Неожиданный алерт'
