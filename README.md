api-django-restframework
===========
It is an implementation of API application, written using django restframework. It implements functionality for authanticating users, adding posts, upvoting, getting info about all this things. The api was containerized into docker. Therefore, you can very quickly untap this API by following the instructions below.

After cloning this repository locally, be sure to add yourself .env file with important keys for the database and for the api server itself inside of current folder. In the following formats:

* POSTGRES_USER = 'user'
* POSTGRES_PASSWORD = 'password'
* POSTGRES_DB = 'database'
* SECRET_KEY = 'secret'
  
Afterwards up docker-compose and check your api http://0.0.0.0/. Actually this app uses nginx proxy for redirecting requests on the http://0.0.0.0:8000/. But 8000 port is not closed and you can check api out there, if you have busy your 80 port with another proxy e.g.
