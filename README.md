# Тестовое задание

В проекте api_yatube есть приложение posts с описанием моделей Yatube. Вам нужно 
реализовать API для всех моделей приложения. 
Обычно всю логику API выносят в отдельное приложение: при иной организации кода 
работать в большом проекте со множеством приложений будет неудобно.  
Добавьте в проект новое приложение с именем "api" и реализуйте всю логику именно 
там. 
API должен быть доступен только аутентифицированным пользователям. Используйте 
в проекте аутентификацию по токену TokenAuthentication. 
Аутентифицированный пользователь авторизован на изменение и удаление своего 
контента; в остальных случаях доступ предоставляется только для чтения. При 
попытке изменить чужие данные должен возвращаться код ответа 403 Forbidden. 

## Установка и запуск

Убедитесь, что у вас установлены Docker и docker-compose.

1. Копирование репозитория:

    ```bash
    git clone https://github.com/MikhalchenkoD/test-task-synctum-django.git
    cd test-task-synctum-django
    ```

2. Установка и запуск (на Window):
   ```bash
   python -m venv venv
   ```
   ```bash
   venv/Scripts/activate
   ```
   ```bash
    pip install -r requirements.txt
    ```
      ```bash
    cd yatube_api
    python manage.py runserver
    ```

3. Установка и запуск (на Linux):
   ```bash
   python3 -m venv venv
   ```
   ```bash
   source venv/bin/activate
   ```
   ```bash
    pip3 install -r requirements.txt
    ```
      ```bash
    cd yatube_api
    python3 manage.py runserver
    ```

## Авторы

Михальченко Дмитрий (https://t.me/DmitriyMikhalchenko)
