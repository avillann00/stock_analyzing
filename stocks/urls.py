# import required modules
from django.urls import path
from . import views

# specific urls for the user views
urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
]
