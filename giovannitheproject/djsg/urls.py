from django.urls import path
from . import views

app_name = 'djsg'
urlpatterns = [
    path('', views.index, name="index"),
    path('sg', views.sg, name="sg"),
    path('tg', views.tg, name="tg"),
    path('result', views.result, name="result"),
    path('shift', views.shift, name='shift'),
    path('shiftslist', views.shiftslist, name='shiftslist'),
    path('timecard', views.timecard, name='timecard'),
    path('ajax', views.ajax, name="ajax"),
]
