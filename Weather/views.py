from django.shortcuts import render,redirect
import requests
from.models import City
from.forms import CityForm
from django.contrib import messages 


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1305f1bb816d36e9866195910b774ee0'
   
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            r = requests.get(url.format(data)).json()
            if r['cod'] == 200:
                if City.objects.filter(name=data).exists():
                    messages.warning(request, "City already exists!")
                else:  
                    form.save()
                    return redirect('/')
            else:
                messages.warning(request,"This City doesn't exists in the World!")
                return redirect('/')
    
    form = CityForm()
    cities = City.objects.all()
    weather_list = []
    
    for city in cities:
    
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature': r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_list.append(city_weather)
        weather_list.reverse()
     
    context = {'weather_list': weather_list,'form':form}
    return render(request,'weather/index.html',context)

def delete(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('/')
