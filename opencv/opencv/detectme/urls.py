#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"), # 웹사이트 링크 home.html
    path("detectme",views.detectme,name="detectme"), # 웹캠 링크
]