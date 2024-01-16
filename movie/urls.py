from django.urls import path
from . import views
urlpatterns = [
    path('movie/', views.MovieListAPIView.as_view()),
    path('', views.DirectorListCreateAPIView.as_view()),
    path('director/', views.director_list_api_view),
    path('reviews/', views.reviews_list_api_view),
    path('<int:id>/', views.movie_list_api_view)
]