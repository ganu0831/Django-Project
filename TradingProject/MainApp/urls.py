from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_csv_view, name ='upload'),
]
