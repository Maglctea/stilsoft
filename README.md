# Stilsoft

Test quest for company stilsoft

<hr/>

## Installation

### Without docker

1) Requirements
    ```bash
    pip install -r requirements.txt
    ```
   
2) Migrations (if there is no database)
   ```bash
   python manage.py migrate
   ```
   
3) Run app
   ```bash 
   python manage.py runserver 
   ```

### With Docker
1) Run docker-compose
   ```bash 
   docker-compose up
   ````
2) After installation, it is available <a href="http://127.0.0.1">here</a>

<hr/>

## Documentation

### Admin panel (Docker)

**Login:** admin@admin.ru

**Password:** admin

### Autodocumentation

1) **Redoc:** <a href="http://127.0.0.1:8000/redoc/">local</a> | <a href="http://127.0.0.1/redoc/">docker</a>

2) **Swagger:** <a href="http://127.0.0.1:8000/swagger/">local</a> | <a href="http://127.0.0.1/swagger/">docker</a>

*See the auto documentation for getting CRUD request parameters*

### Transaction
* **GET:** <a href="http://127.0.0.1:8000/api/transactions/">local</a> | <a href="http://127.0.0.1/api/transactions/">docker</a> - all transactions

* **GET/PUT/DELETE:** http://127.0.0.1:8000/api/transactions/<id:int> (local) | http://127.0.0.1/api/transactions/<id:int> (docker) - detail view transaction

### User
* **GET POST:** <a href="http://127.0.0.1:8000/api/users/">local</a> | <a href="http://127.0.0.1/api/users/">docker</a> - all users

* **GET/PUT/DELETE:** http://127.0.0.1:8000/api/users/<id:int> (local) | http://127.0.0.1/api/users/<id:int> (docker) - detail view user

* **GET:** <a href="http://127.0.0.1:8000/api/users/top-max/">local</a> | <a href="http://127.0.0.1/api/users/top-max/">docker</a> - viewing top-10 users with max transactions

* **GET:** <a href="http://127.0.0.1:8000/api/users/top-max/">local</a> | <a href="http://127.0.0.1/api/users/top-max/">docker</a> - viewing top-10 users with total sum transactions


