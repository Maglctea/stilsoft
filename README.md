# Stilsoft

Test quest for company stilsoft

<hr/>

## Installation
1) Requirements
    ```bash
    pip install -r requirements.txt
    ```
   
2) Migrations (if there is no database)
   ```bash
   python manage.py migrate
   ```
   
## Run app
   ```bash 
   python manage.py runserver 
   ```

<hr/>

## Documentation

### Autodocumentation

1) **Redoc:** http://127.0.0.1:8000/redoc/

2) **Swagger:** http://127.0.0.1:8000/swagger/

### Transaction
* **GET:** http://127.0.0.1:8000/api/transactions/ - all transactions

* **GET/PUT/DELETE:** http://127.0.0.1:8000/api/transactions/<id:int> - detail view transaction

### User
* **GET POST:** http://127.0.0.1:8000/api/users/ - all users

* **GET/PUT/DELETE:** `http://127.0.0.1:8000/api/users/<id:int> - detail view user

* **GET:** http://127.0.0.1:8000/api/users/top-max/ - viewing top-10 users with max transactions

* **GET:** http://127.0.0.1:8000/api/users/top-max/ - viewing top-10 users with total sum transactions


