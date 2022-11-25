from django.urls import path

from homeapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('user',views.user,name='user'),
    path('worker',views.worker,name='worker'),
    path('userregister',views.userregister,name='userregister'),
    path('workerregister',views.workerregister,name='workerregister'),
    path('user_button',views.user_button,name='user_button'),
    path('view_user',views.view_user,name='view_user'),
    path('worker_button',views.worker_button,name='worker_button'),
    path('view_worker', views.view_worker, name='view_worker'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user')

]