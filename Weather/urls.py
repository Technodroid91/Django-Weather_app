from django.urls import path,include
from Weather.views import index,delete



urlpatterns = [

    path('',index,name='index'),
    path('delete/<city_name>/',delete,name='delete_city'),

    ]

#http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={1305f1bb816d36e9866195910b774ee0}
