from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('posts/', include('posts.urls')),
    path("comments/", include('comments.urls')),
    path("votes/", include('votes.urls'))
]
