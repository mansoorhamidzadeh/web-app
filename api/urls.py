from django.urls import  path
from . import views

urlpatterns=[
    path('list/',views.PostApiView.as_view())
]