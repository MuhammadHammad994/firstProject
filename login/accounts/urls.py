from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns=[
    path('',views.indexView,name='index.html'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('register/',views.registerView,name='register_url'),
    #path('logout',),
]
