amazingco2
==========

This is a code sample for TradeShift. Because I know you'll be building with Docker, I'll include the instructions for how to build and run the app below.::

  $ docker-compose -f local.yml build
  $ docker-compose -f local.yml up

You can browse the API visually by navigating to http://localhost:8000/api/nodes/1/. You can also use cURL::

  $ curl -X GET http://localhost:8000/api/nodes/1/ | json_pp

For the response::

  {
    "pk": 1,
    "descendants": [],
    "root": null,
    "level": 0,
    "parent": null
  }
  
To make a new node with its parent set as the root node, you can run the following cURL request::

  $ curl -X POST http://localhost:8000/api/nodes/ -H 'Content-Type: application/json' -d '{"parent": 1}' | json_pp

You should get back the following response body::

  {
    "pk": 2,
    "descendants": [],
    "root": 1,
    "level": 1,
    "parent": 1
  }

Go ahead and re-run the first cURL command again. You'll get back::

  {
   "parent" : null,
   "descendants" : [
      {
         "parent" : 1,
         "pk" : 2,
         "level" : 1,
         "root" : 1
      }
   ],
   "level" : 0,
   "pk" : 1,
   "root" : null
  }

If you run the POST command again, but this time set the parent attribute as 2, you'll get back the following::

  {
    "pk": 3,
    "descendants": [],
    "root": 1,
    "level": 2,
    "parent": 2
  }

To update a node, you can use the following cURL request::

  $ curl -X PATCH http://localhost:8000/api/nodes/3/ -H 'Content-Type: application/json' -d '{"parent": 1}' | json_pp

For the following response::

  {
    "parent": 1,
    "pk": 3,
    "descendants": [],
    "root": 1,
    "level": 1
  }

You can view the root node again::

  $ curl -X GET http://localhost:8000/api/nodes/1/

For the following response::

  {
    "parent": null,
    "pk": 1,
    "descendants": [2, 3],
    "root": null,
    "level": 0
  }

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy amazingco2

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



