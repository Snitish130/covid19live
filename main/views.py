from django.shortcuts import render
import requests



def home(request):
    data = request.POST.get('name')


    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":data}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data= response['response']
    d=data[0]


    context = {
    'country': d['country'],
    'all': d['cases']['total'],
    'recovered': d['cases']['recovered'],
    'deaths': d['deaths']['total'],
    'newdeaths': d['deaths']['new'],
    'new': d['cases']['new'],
    'active': d['cases']['active'],
    'critical': d['cases']['critical']

    }
    return render(request,'index.html' , context)
