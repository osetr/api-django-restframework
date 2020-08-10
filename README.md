api-django-restframework
===========
It is an implementation of API application, written using django restframework. It implements functionality for authanticating users, adding posts, upvoting, getting info about all this things. The api was containerized into docker. Therefore, you can very quickly untap this API by following the instructions below.

After cloning this repository locally, be sure to add yourself .env file with important keys for the database and for the api server itself inside of current folder. In the following formats:

* POSTGRES_USER = 'user'
* POSTGRES_PASSWORD = 'password'
* POSTGRES_DB = 'database'
* SECRET_KEY = 'secret'
  
Afterwards up docker-compose and check your api http://0.0.0.0/. Actually this app uses nginx proxy for redirecting requests on the http://0.0.0.0:8000/. But 8000 port is not closed and you can check api out there, if you have busy your 80 port with another proxy e.g.

api-documentation
-----------------
Here you can find requests, which you are able to do with this api. Actually, it's just a general view of them, for more detail info you can follow link on the [postman collection](https://www.getpostman.com/collections/220dab40d84b3242401b), that can give you more concsious view.

<dl>
  <dt>/auth/</dt>
    <dd>/api/v1/auth/users/ - POST for adding new user, available for all users, ('username', 'email', password') fields in body are required<dd>
    <dd>/api/v1/auth/jwt/create/ - POST for authorizating using jwt access&refresh tokens, ('username', password') fields in body are required<dd>
    <dd>/api/v1/auth/jwt/refresh/ - POST for refreshing access token, ('refresh') field in body are required<dd>
  <dt>/users/</dt>
    <dd>/api/v1/users/all/ - GET for getting all users list, only for authanticated admin users</dd>
  <dt>/posts/</dt>
    <dd>/api/v1/posts/all/ - GET for getting all posts list, only for authanticated admin users</dd>
    <dd>/api/v1/posts/post/create/ - POST for creating new post, only for authenticated users, ('title', content') fields in body are required<dd> 
    <dd>/api/v1/posts/post/detail/<post_id>/ - GET for getting info about post<dd>
    <dd>/api/v1/posts/post/detail/<post_id>/ - DELETE for deleting post, only for post owner<dd>
    <dd>/api/v1/posts/post/detail/<post_id>/ - PUT for updating post data, ('title', content') fields in body are required<dd>
  <dt>/votes/</dt>
    <dd>/api/v1/votes/all/ - GET for getting all votes list, only for authanticated admin users</dd>
    <dd>/api/v1/votes/vote/<post_id>/ - POST for upvoting post, only for authenticated users<dd> 
  <dt>/comments/</dt>
    <dd>/api/v1/comments/comment/post/<post_id>/ - POST for comment post, only for authanticated users, ('content') field in body are required</dd>
    <dd>/api/v1/comments/all/ - GET for getting all comments list, only for authanticated admin users<dd>
    <dd>/api/v1/comments/comment/<comment_id>/ - GET for getting comment info, only for authanticated admin users<dd>
    <dd>/api/v1/comments/comment/<comment_id>/delete/ - DELETE for deleting comment, only for comment owner<dd>
    <dd>/api/v1/comments/comment/<comment_id>/update/ - PUT for updating comment, only for comment owner<dd>
</dl>
