from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('',views.HomePage,name='homepage' ),
    path('insert/',views.InsertStudent,name='insert'),
    path('update_all/',views.UpdateStudent,name='update_all'),
    path('delete_data/',views.delete_data,name='delete_data'),
]