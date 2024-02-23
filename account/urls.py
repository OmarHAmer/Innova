from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('',views.redirectHome,name='redirectHome'),
    path('<str:app>/<str:slug>',views.navpage,name='navpage'),
]