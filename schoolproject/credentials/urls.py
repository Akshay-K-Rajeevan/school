from django.urls import path
from .import views
urlpatterns = [
path('',views.home, name ='home'),
path ('register',views.register, name = 'register'),
path ('login',views.login, name='login'),
path ('store',views.store,name ='store'),
path ('order',views.order,name ='order'),
path('logout',views.logout,name='logout'),
path ('confirm',views.confirm,name='confirm')
    ]