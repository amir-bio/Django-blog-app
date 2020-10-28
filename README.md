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



TODOs:
 - [x] API Documentation ideally redoc
 - [ ] Custom Permission checks
 - [ ] Custom authentication (ideally google auth) - look into djoser lib and maybe authentication with custom pw with signup via welcome email
 - [ ] Add Github Actions
 - [ ] Play around with several different python toolings for linting, auditing, depency checks
 - [ ] setup depend bot on github
 - [ ] Find a platform to deploy this to - mainly looking to do it with terrafrom
 - [ ] maybe play around with deploying it as AWS Lambda and playaround with that
 - [ ] setup docker and docker compose for realistic DB
 - [ ] Push docker images to github container registry
 - [ ] play around with a live database
 - [ ] Research API test - I recall Tavern API testing as being a good option and  look into contract testing
 - [ ] Redis Caching
 - [ ] Celery/Redis message queue
