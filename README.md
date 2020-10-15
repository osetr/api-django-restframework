api-django-restframework
===========

description
-----------
It is an implementation of an API application, written using django restframework. It implements functionality for authenticating users, adding posts, upvoting, getting info about all such things. The api was containerized into docker. Therefore, you can very quickly untap this API by following the instructions below.

After cloning this repository locally, be sure to add yourself .env file with important keys for the database and for the api server itself inside of the current folder. In the following formats:

```
* POSTGRES_USER = 'user'
* POSTGRES_PASSWORD = 'password'
* POSTGRES_DB = 'database'
* SECRET_KEY = 'secret'
* VOTES_RESET_TIMEDELTA = '1440' (reset post upvotes count once per 1440 minutes)
```
  
Afterwards up docker-compose and check your API http://0.0.0.0/. Actually this app uses nginx proxy for redirecting requests on the http://0.0.0.0:8000/. But 8000 port is opened and you can check API out there, if you have your 80 port busy with another proxy e.g.

api-documentation
-----------------
Here you can find requests, that you can make with this API. Actually, it's just a general overview of them, for more detailed info you can follow link on the [postman collection](https://www.getpostman.com/collections/220dab40d84b3242401b), it can give you more concsious overview.

```sh
  * /auth/
    /api/v1/auth/users/ - POST for adding new user, available for all users, ('username', 'email', password') fields in body are required
    /api/v1/auth/jwt/create/ - POST for authorizating using jwt access&refresh tokens, ('username', password') fields in body are required
    /api/v1/auth/jwt/refresh/ - POST for refreshing access token, ('refresh') field in body are required
  * /users/
    /api/v1/users/all/ - GET for getting all users list, only for authanticated admin users
  * /posts/
    /api/v1/posts/all/ - GET for getting all posts list, only for authanticated admin users
    /api/v1/posts/post/create/ - POST for creating new post, only for authenticated users, ('title', content') fields in body are required 
    /api/v1/posts/post/detail/<post_id>/ - GET for getting info about post
    /api/v1/posts/post/detail/<post_id>/ - DELETE for deleting post, only for post owner
    /api/v1/posts/post/detail/<post_id>/ - PUT for updating post data, ('title', content') fields in body are required
  * /votes/
    /api/v1/votes/all/ - GET for getting all votes list, only for authanticated admin users
    /api/v1/votes/vote/<post_id>/ - POST for upvoting post, only for authenticated users 
  * /comments/
    /api/v1/comments/comment/post/<post_id>/ - POST for comment post, only for authanticated users, ('content') field in body are required
    /api/v1/comments/all/ - GET for getting all comments list, only for authanticated admin users
    /api/v1/comments/comment/<comment_id>/ - GET for getting comment info, only for authanticated admin users
    /api/v1/comments/comment/<comment_id>/delete/ - DELETE for deleting comment, only for comment owner
    /api/v1/comments/comment/<comment_id>/update/ - PUT for updating comment, only for comment owner
```
