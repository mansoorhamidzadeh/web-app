from django.urls import path
from . import views
app_name='account'
urlpatterns=[
    path('login/',views.login_user,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('profile/',views.ProfileView,name='profile'),
    path('register/',views.register_user,name='register')
]