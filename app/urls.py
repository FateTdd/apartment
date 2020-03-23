from django.urls import path
from app import views

app_name = 'apartment'

urlpatterns = [
    path('apartment/<int:apartmentid>/', views.apartmentview, name='index'),
    path('collection/', views.collection, name='collection'),
    path('collect/', views.collect, name='collect'),
    path('cancelcollect/<int:apartmentid>/', views.cancelcollect, name='cancelcollect'),
    path('search/', views.search, name='search'),
    path('', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('registerview/', views.registerview, name='registerview'),
    path('register/', views.register, name='register'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('forgetpwd/', views.forgetpwd, name='forgetpwd'),

]