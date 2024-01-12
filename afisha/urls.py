
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    path('/api/v1/directors/'), include('movie.urls'),
    path('/api/v1/directors/<int:id>/'), include('movie.urls'),

    path('/api/v1/movies/'), include('movie.urls'),
    path('/api/v1/movies/<int:id>/'), include('movie.urls'),
    path('/api/v1/movies/reviews/'), include('movie.urls'),

    path('/api/v1/reviews/'), include('movie.urls'),
    path('/api/v1/reviews/<int:id>/'), include('movie.urls'),
    path('api/v1/users/', include('users.urls')),
]
