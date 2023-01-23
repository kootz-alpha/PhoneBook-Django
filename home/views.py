from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home.models import User, Contact
from django.template.defaulttags import csrf_token



# Create your views here.

def login(request) :
    if request.method == "POST" :
        u = User.objects.get(uname=request.POST["username"])
        pw = u.pwrd

        if pw == request.POST["password"] :

            contacts = Contact.objects.filter(user=u)

            return render(request, 'home.html', {'contacts':contacts, 'username':u.uname})

    return HttpResponse("No user")

def signup(request) :
    if request.method == "POST" :
        u = request.POST["username"]
        pw = request.POST["password"]

        User.objects.create(uname=u, pwrd=pw)
        c = []
        return render(request, 'home.html', {'contacts':c, 'username':u})

    return HttpResponse("Invalid Request")

def load(request) :

    template = loader.get_template('main.html')
    return render(request, 'main.html')

def add(request) :
    if request.method == "POST" :
        u = User.objects.get(uname=request.POST["username"])
        Contact.objects.create(user=u, name=request.POST["name"], phone_number=request.POST["phone"])
        c = Contact.objects.filter(user=u)
        response = render(request, 'home.html', {'contacts':c, 'username':u.uname})
        response["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response["Pragma"] = "no-cache"
        response["Expires"] = "0"
        return response

    return HttpResponse("Invalid Request")

def dele(request) :
    if request.method == "POST" :
        u = User.objects.get(uname=request.POST["username"])
        Contact.objects.filter(user=u, name=request.POST["name"]).delete()
        c = Contact.objects.filter(user=u)
        return render(request, 'home.html', {'contacts':c, 'username':u.uname})

    return HttpResponse("Invalid Request")

def search(request) :
    if request.method == "POST" :
        text = request.POST["text"]
        u = User.objects.get(uname=request.POST["username"])
        c = Contact.objects.filter(user=u)
        a = []

        if len(text) == 0 :
            return render(request, 'home.html', {'contacts':c, 'username':u.uname})

        for element in c :
            if element.name[ : len(text)] == text :
                a.append(element)

        return render(request, 'home.html', {'contacts':a, 'username':u.uname})

    return HttpResponse("Invalid Request")

