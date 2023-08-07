from . import views
from django.urls import path


urlpatterns = [
    path('authorization/', views.AthorizationAPIView.as_view(), name='authorization'),
    path('registration/', views.registration_api_view, name='registration'),
]