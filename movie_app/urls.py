from . import views
from django.urls import path

urlpatterns = [
    path('', views.DirectorListCreateAPIView.as_view()),
    path('<int:id>/', views.director_detail_api_view),
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieListCreateAPIView.as_view()),
    path('reviews/', views.ReviewModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reviews/<int:id>/', views.ReviewModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                'delete': 'destroy'}))
]