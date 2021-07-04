Carsapp 
=======

Application gets cars from https://vpic.nhtsa.dot.gov/api/ and save it in local database.

-------

How to run:
-----------
    git clone https://github.com/retarf/carapp
    cd carapp
    create .env file (you can use env.example file as example)
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose up

-----------

Usage:
------
    POST /cars     -- add car to local database if car exists in https://vpic.nhtsa.dot.gov/api/
                      If the car doesn't exist - return an error
    POST /rate     -- Add a rate for a car from 1 to 5
    GET /cars      -- display list of all cars already present in database with their current average rate
    GET /popular   -- return top cars already present in the database ranking based on number of rates

------

How to run tests:
----------------
    docker-compose run web python manage.py test

----------------

Requirements:
-------------
* django==3.2
* psycopg2-binary==2.9.1
* djangorestframework==3.12
* gunicorn==20.1
* django-environ-2==2.1
* whitenoise==5.2

-------------

