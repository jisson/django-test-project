# Django test project

A Django demo project that expose a simple REST API, allowing to browse users and their listings.

## About

The purpose of this project is to use a maximum of Django and DRF features in order to build a simple API, covered by
tests, with an easy to read documentation.

This project is built in python upon the following libraries:
 - [Django](https://www.djangoproject.com/).
 - [Django Rest Framework](https://www.django-rest-framework.org/).
 
Additionally, it uses:
 - [Django extensions](https://django-extensions.readthedocs.io/en/latest/) to add some helpful commands such as `shell_plus` and `runserver_plus`.
 - [DRF Yasg](https://github.com/axnsan12/drf-yasg) to generate the documentation by using [ReDoc](https://redoc.ly/).
 - [Factory Boy](https://factoryboy.readthedocs.io/en/latest/) to easily populate the database with test data.
 - [Freeze gun](https://github.com/spulec/freezegun) to ease the manipulation of the time during the unit tests.
 - [black](https://github.com/psf/black) to unify the formatting of the code.
 - [isort](https://pypi.org/project/isort/) to unify the order of the imports.

 ## Models
 
 This project expose two models:
  - `Listing`: have a label, a status and should be linked to a `User`. A `Listing` is considered as `active` if its status is `published` and if 
  its user is active.
  - `ListingOwner`: A `proxy` model derivated from the django auth user. A `User` is considered as a `ListingOwner` if it has at least a `Listing`.
  
 ## How to install
 
 ### By using docker-compose
 
 The easiest way to setup the project is to use [docker-compose](https://docs.docker.com/compose/install/):
 
 ```bash
docker-compose up -d
 ```
*Note*: The `-d` option is for `detached`. It could be used to run the django server as a background task but it is not mandatory.

This would build the image and install the requirement. The `Dockerfile` is build upon `python 3.7`.
Dont forget to run the migrations:

```bash
docker-compose run django-test-project migrate
```

It is possible to run a python shell by using the following command:
```bash
docker-compose run django-test-project shell_plus
```

All the managements commands are accessible by using `docker-compose run django-test-project {command-name}`.

The server should be accessible at [http://127.0.0.1:8000]().

### By installing the requirements

*Note*: This project as been built by using `python 3.7`. It is advised to run the following commands in a fresh 
virtualenv by using this version of Python.

First, we have to install the requirements of the project:
```bash
pip install -r requirements/dev.txt
```
run, the migrations:
```bash
python manage.py migrate
```
and, finally, run the server:
```
python manage.py runserver_plus
```

The server should be accessible at [http://127.0.0.1:8000]().

### Create the test data

A management command named `create_test_data` is available under the `listings` app. Depending on the installation 
method you chose, just run:
```bash
# docker-compose
docker-compose run django-test-project create_test_data
# virtualenv
python manage.py create_test_data
```

It will create few users with listings as well as an admin user named `demo`. You can now login to the admin with 
the following credentials:
 - username: `demo`
 - password: `password`
 
This user could be used to browse views that are restricted to admin people.

## Use the API.

The API documentation is available on [127.0.0.1:8000/redoc/]().

*Note*: the examples below are using `curl`, but you can access to a graphical interface allowing to query the API
by simply copy the url of the endpoint into a web browser.

### Fetch the listings owners

```bash
curl http://127.0.0.1:8000/users/owners/
```

### Fetch the listings

#### Fetch all the listings

*Note*: accessing all the listings require to be logged in as an admin user. We don't want that `draft` and `unpublished`
to be public.

```bash
curl --user demo:password http://127.0.0.1:8000/listings/
```

#### Fetch active listings

*Note*: this endpoint is accessible to any one.

```bash
curl http://127.0.0.1:8000/listings/active/
```

#### Filter on listings

*Note*: At the exception of the `status` filter, filters could be used on both `active` and `all` listings endpoints.

Filter listings by their `status`:
```bash
curl http://127.0.0.1:8000/listings/?status=draft --user demo:password
```

Choices are: `draft`, `published`, `unpublished`.

Filter listings by their owner:
```bash
curl http://127.0.0.1:8000/listings/?owner={owner_id} --user demo:password
```
where `owner` is the primary key of the listing owner.

Search among listing's titles:
```bash
curl http://127.0.0.1:8000/listings/?search=Search+term --user demo:password
```

Sort listings by publication date (descending):
```bash
curl http://127.0.0.1:8000/listings/?ordering=-published_at --user demo:password
```
