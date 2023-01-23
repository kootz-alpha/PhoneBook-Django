from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('sign', views.signup, name="signup"),
    path('add', views.add, name='add'),
    path('del', views.dele, name='del'),
    path('search', views.search, name='search')
]