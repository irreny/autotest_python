import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv('URL')
TOKEN = os.getenv('TRAINER_TOKEN_PROD')
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
    }
TRAINER_ID = os.getenv('TRAINER_ID_PROD')
BODY = {
    "name": "irreny",
    "city": "Kioto"
}


def test_status_code():
    """GET-запрос к ресурсу /trainers возвращает HTTP-статус 200 (OK)."""
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200


@pytest.mark.xfail(reason='Fix bug #1234')
def test_put_trainer(key, value):
    """PUT-запрос к ресурсу /trainers."""
    response = requests.put(url=f'{URL}/trainers', headers=HEADER, json=BODY)
    assert response.status_code == 422


@pytest.mark.parametrize('key, value', [('trainer_name', 'irreny')])
def test_trainer_name(key, value):
    """Значение указанного ключа в ответе API соответствует ожидаемому значению

    Параметры:
    key (str): Ключ, который проверяется в JSON-ответе.
    value (str): Ожидаемое значение для указанного ключа.
    """
    response = requests.get(url=f'{URL}/trainers/38037')
    json_resp = response.json()
    assert key in json_resp, f"Ключ '{key}' отсутствует в ответе: {json_resp}"
    assert json_resp[key] == value
