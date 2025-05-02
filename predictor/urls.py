from django.contrib import admin
from django.urls import path
from predictor import views
import sys

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('predictors/', views.predictor, name='predictor'), 
    path('about/', views.about, name='about'), 
    path('predict_1/', views.predictor_view_1, name='predict_1'), 
    path('predict_2/', views.predictor_view_2, name='predict_2'),
]
