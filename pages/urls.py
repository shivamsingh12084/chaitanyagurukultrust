from django.urls import path
from . import views

from .views import *

urlpatterns = [
    path('', views.HomePageView, name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('admission/', views.Admission, name="admission"),
    path('academics/', views.Acadimics, name="academics"),
    path('alumni/', views.Alumni, name="alumni"),
    path('career/', views.Career, name="career"),
    path('cgtOverview/', views.CgtOverview, name="cgtOverview"),
    path('chaitanyaMeaning/', views.ChaitanyaMeaning, name="chaitanyaMeaning"),
    path('coCurricular/', views.CoCurricular, name="coCurricular"),
    path('mentors/', views.Mentors, name="mentors"),
    path('boards/', views.Boards, name="boards"),
    path('socialservice/', views.SocialService, name="socialservice"),
    path('trips/', views.Trips, name="trips"),
    path('vission/', views.Vission, name="vission"),
    path('physical/', views.Physical, name="physical")
]