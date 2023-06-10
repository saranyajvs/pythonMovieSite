from . import views
from django.urls import path

app_name = 'movieapp'  # namespace
urlpatterns = [
    path('', views.index, name='index'),
    # path('movie/<int:movie_id>/',views.details, name='details'), # to get url as movie/1
    path('movie/<int:movie_id>/', views.showdetails, name='showdetails'),  # to get url as movie/1
    path('add/', views.addMovie, name='addMovie'),
    path('edit/<int:movie_id>/', views.editMovie, name='editMovie'),
    path('delete/<int:movie_id>/', views.deleteMovie, name='deleteMovie')
]
