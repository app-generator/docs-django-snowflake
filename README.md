# [Django & Snowflake Integration](https://app-generator.dev/docs/technologies/django/integrate-snowflake.html)

Coding sample for **Django & Snowflake Integration** documentation page.
 
## Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/docs-django-snowflake.git
$ cd docs-django-snowflake
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

Enter Snowflake informations in the .env file. 

```bash
SNOWFLAKE_USER="your_username"
SNOWFLAKE_PASSWORD="your_password"
SNOWFLAKE_ACCOUNT="your_account_identifier"
SNOWFLAKE_WAREHOUSE="your_warehouse"
SNOWFLAKE_DATABASE="your_database"
SNOWFLAKE_SCHEMA="your_schema"
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
**[Django & Snowflake Integration](https://app-generator.dev/docs/technologies/django/integrate-snowflake.html)** - Coding sample provided by **[App Generator](https://app-generator.dev/)**
