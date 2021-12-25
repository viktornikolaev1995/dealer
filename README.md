# Honest Dealer
Сайт о дилерах и дилерских центрах
## Описание
+ Просмотр всех дилеров, доступных на сайте
  ![dealers](https://github.com/viktornikolaev1995/dealer/blob/test/images_for_README/dealers_list.png "dealers")
+ Просмотр всех дилерских центров и закрепленных за ними услугами
  ![dealer_centers](https://github.com/viktornikolaev1995/dealer/blob/test/images_for_README/dealer_centers_list.png "dealer_centers")
+ Просмотр детальной информации о конкретном дилерском центре
  ![dealer_center](https://github.com/viktornikolaev1995/dealer/blob/test/images_for_README/dealer_center_detail.png "dealer_center")  
+ Каждый автомобиль может принадлежать только одному дилерскому центру и соответственно только одному дилеру
+ На странице с конкретным дилерским центром можно оставлять отзывы и также отвечать на них
+ Просмотр автомобилей нового модельного ряда
  ![new_vehicles](https://github.com/viktornikolaev1995/dealer/blob/test/images_for_README/vehicles_list.png "new_vehicles")  
+ Просмотр автомобилей с пробегом  
+ Просмотр автомобилей нового модельного ряда, принадлежащих конкретному дилерскому центру
+ Просмотр автомобилей с пробегом, принадлежащих конкретному дилерскому центру
+ Просмотр детальной информации об автомобиле нового модельного ряда
+ Просмотр детальной информации об автомобиле с пробегом
  ![vehicle_with_mileage](https://github.com/viktornikolaev1995/dealer/blob/test/images_for_README/vehicle_detail.png "vehicle_with_mileage") 

## Инструкция по развертыванию проекта
1. Скачать проект или клонировать с помощью git (`git clone https://github.com/viktornikolaev1995/dealer.git`)
2. Перейти в каталог с проектом и создать виртуальное окружение (`python3 -m venv venv`)
3. Запустить виртуальное окружение (`source venv/bin/activate`) на Mac/Linux (`source venv/Scripts/activate`) на Windows
4. Установить все необходимые пакеты, указанные в файле requirements.txt (`pip install -r requirements.txt`)
5. В данном проекте использовалась СУБД PostgreSQL, для ее настройки нужно пройти пункты с 6-10 
6. Перейти в терминал sql-shell под пользователем postgres (`psql -U postgres`)   
7. Создать базу данных (`CREATE DATABASE dealer_db;`)
8. Создание пользователя (`CREATE USER dealer_user WITH PASSWORD 'dealer_user_password';`)
9. Предоставить пользователю dealer_user привилегии к базе данных dealer_db (`GRANT ALL PRIVILEGES ON DATABASE dealer_db TO dealer_user;`)   
10. В корневом каталоге проекта в файле settings.py изменить при необходимости данные об имени базы данных (`'NAME': dealer_db`), пользователе (`'USER': 'dealer_user'`), пароле (`'PASSWORD': 'dealer_password'`)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dealer_db',
        'USER': 'dealer_user',
        'PASSWORD': 'dealer_user_password',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```
11. Запустить миграции (`python manage.py migrate`)
12. Перейти по адресу http://127.0.0.1:8000
