from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    #url="http://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22"
    api_req = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={c024db4252df483d3b82b661c1c4bb7f}")
    try:
        api = json.load(api_req.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})

