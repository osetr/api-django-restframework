from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/posts/', include('posts.urls')),
    path("api/v1/comments/", include('comments.urls')),
    path("api/v1/votes/", include('votes.urls')),
    path("api/v1/users/", include('users.urls')),
]
