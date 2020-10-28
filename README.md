# Django Blog App

This is a small project to create an API for a blog created with Django and
Django REST framework.

This project uses `pipenv` for virtual env and package management.

To run the API server locally:
```sh
pipenv shell # create shell insisde venv (creates a venv, installs packages if needed)
python manage.py migrate # only necessary once at the start and after every model change
python manage.py runserver
```

API root: http://127.0.0.1:8000/api/v1/ [When accessed by a web browser shows an
interactive API browsing tool]

Redoc API documentation: http://127.0.0.1:8000/api/v1/redoc/

Screenshot of the Redoc API doc:
![Redoc](./redoc.PNG)
