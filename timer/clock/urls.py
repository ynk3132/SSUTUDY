from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clock/', views.clock, name='clock'),
    path('hello/', views.hello, name='hello'),
    path('pomo/', views.pomo, name='pomo'),
    path('test1/', views.test1, name='test1'),
    path('stopwatch/', views.stopwatch, name='stopwatch'),
    path('check/', views.check, name='check'),
    path('ajax/', views.ajax, name='ajax'),
    path('ajax/send', views.send, name='send'),
]