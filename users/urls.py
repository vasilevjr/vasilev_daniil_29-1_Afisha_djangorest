from . import views
from django.urls import path


urlpatterns = [
    path('authorization/', views.authorization_api_view, name='authorization'),
    path('registration/', views.registration_api_view, name='registration'),
]