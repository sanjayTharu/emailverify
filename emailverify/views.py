from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    if request.method == "POST":
        domain = request.POST.get('domain')
        url = "https://mailcheck.p.rapidapi.com/"
        querystring = {"domain":domain}

        headers = {
            "X-RapidAPI-Key":"",
            "X-RapidAPI-Host":""
        }

        response = requests.request("GET",url,headers=headers,params=querystring).json()
        valid = response['valid']
        block = response['block']
        disposable = response['disposable']
        domain = response['domain']
        text = response['text']
        reason = response['reason']
        risk = response['risk']
        mx_host = response['mx_host']
        mx_ip = response['mx_ip']
        mx_info = response['mx_info']
        last_changed_at = response['last_changed_at']

        context = {
            'valid':valid,
            'block':block,
            'disposable':disposable,
            'domain': domain,
            'text':text,
            'reason': reason,
            'risk':risk,
            'mx_host':mx_host,
            'mx_ip':mx_ip,
            'mx_info':mx_info,
            'last_changed_at':last_changed_at
        }

        return render(request, "emailverify/index.html",context)
    return render(request, "emailverify/index.html")
