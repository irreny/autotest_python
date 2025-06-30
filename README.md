# 🧪 Пример автотестов на `pytest` + `requests` + `selenium`

## 📋 Описание

Этот проект демонстрирует написание автоматизированных тестов для API и UI сервиса [Pokemon Battle](https://pokemonbattle.ru). В тестах используются:

- [`pytest`](https://en.wikipedia.org/wiki/Pytest) — тестовый фреймворк
- [`requests`](https://en.wikipedia.org/wiki/Requests_(software)) — работа с HTTP-запросами
- [`selenium`](https://en.wikipedia.org/wiki/Selenium_(software)) — автоматизация браузера
- [`loguru`](https://github.com/Delgan/loguru) — логирование
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — управление переменными окружения

---

## 🧰 Установка

```bash
git clone git@github.com:irreny/autotest_python.git
cd autotest_python

python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

pip install -r requirements.txt
```

Также убедитесь, что установлен ChromeDriver или аналогичный драйвер под ваш браузер.

🔐 Настройка .env

Создайте .env файл на основе .env.example:

```
cp .env.example .env
```
И укажите в нем:
```
TRAINER_TOKEN_PROD=your_token_here
TRAINER_ID_PROD=your_trainer_id_here

USER_LOGIN=your_email@example.com
USER_PASS=your_password_here

INCORRECT_LOGIN=your_fall_email@example.com
INCORRECT_PASS=your_fall_password_here
```

✅ Запуск тестов
Запуск API тестов:
```
pytest tests
```
