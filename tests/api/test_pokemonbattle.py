import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
    }
TRAINER_ID = '38037'


def test_status_code():
    """GET-запрос к ресурсу /trainers возвращает HTTP-статус 200 (OK)."""
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200


@pytest.mark.parametrize('key, value', [('trainer_name', 'irreny')])
def test_trainer_name(key, value):
    """Значение указанного ключа в ответе API соответствует ожидаемому значению

    Параметры:
    key (str): Ключ, который проверяется в JSON-ответе.
    value (str): Ожидаемое значение для указанного ключа.
    """
    response = requests.get(url=f'{URL}/trainers/{TRAINER_ID}')
    assert response.json()[key] == value
