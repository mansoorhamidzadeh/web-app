from django.urls import  path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:pk>/',views.detail,name='detail'),
    path('create/',views.createview,name='create'),
    path('update/<int:pk>/',views.updateview,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('userpost/<str:username>/',views.user_post,name='userpost')
]