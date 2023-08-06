from . import views
from django.urls import path

urlpatterns = [
    path('', views.director_list_api_view),
    path('<int:director_id>/', views.director_detail_api_view),
    path('', views.movie_list_api_view),
    path('<int:movies_id>/', views.movie_detail_api_view),
    path('', views.review_list_api_view),
    path('<int:review_id>/', views.review_detail_api_view),
]