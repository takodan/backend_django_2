from django.urls import path, re_path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("wah/", views.wah),
    path("HTTPinfo/", views.HTTPinfo),
    path("wah/<str:params1>", views.wah_with_params),
    path('re_wah/10', views.wah_with_params)
]