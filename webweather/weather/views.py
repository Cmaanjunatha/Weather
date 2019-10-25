from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    #url="http://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22"
    api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282")
    try:
        api = json.load(api_req.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})

def about(request):
    import json
    import requests
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=c024db4252df483d3b82b661c1c4bb7f='
    #city = input('City Name :')
    city = input('Bengaluru')
    url = api_address + city
    json_data = requests.get(url).json()
    api = json_data['base']
    #print(format_add)
    return render(request, 'about.html', {'api': api})

