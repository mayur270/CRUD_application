# CRUD_application

Django CRUD application where one could add/delete/alter employee contact details.

**USERNAME:** admin <br>
**PASSWORD:** testpass123 <br>
**LIVE_DEMO:** https://rocky-caverns-53277.herokuapp.com/

To run the application:
1. In your editor, run Pipenv install Django
2. Enter development environment with Pipenv Shell
3. Then install all dependencies with Pipenv install
4. Then run Python manage.py runserver

In this project, employees is the directory level folder. Other apps includes
contacts which is the main app and users app for authentication. SQlite was
used as the database in this project. Although, the database can be easily
replaced with Postgre DB by changing the following codes in the settings file:

DATABASES = {<br>
    'default': {<br>
    'ENGINE': 'django.db.backends.postgresql',<br>
    'NAME': 'postgres',<br>
    'USER': username,<br>
    'PASSWORD': user_password,<br>
    'HOST': '127.0.0.1',<br>
    'PORT': 5432<br>
    }
}
