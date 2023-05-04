from django.urls import  path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:pk>/',views.detail.as_view(),name='detail'),
    path('create/',views.createview.as_view(),name='create'),
    path('update/<int:pk>/',views.updateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.delete.as_view(),name='delete'),
    path('userpost/<str:username>/',views.user_post.as_view(),name='userpost')
]