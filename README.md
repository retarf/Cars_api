Carsapp 
=======

Application gets cars from https://vpic.nhtsa.dot.gov/api/ and save it in local database.

-------

How to run:
-----------
    git clone https://github.com/retarf/carapp
    cd carapp
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

Requirements:
-------------
* django==3.0
* psycopg2==2.8.5
* django-rest-framework
* gunicorn
* django-heroku

-------------

