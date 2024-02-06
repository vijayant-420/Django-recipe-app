from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {'name': 'Vijayant Singh', 'age':24},
        {'name': 'Sanskar', 'age':34},
        {'name': 'David', 'age':28},
        {'name': 'Tushar', 'age':26},
        {'name': 'Vineet', 'age':14}
    ]
    
    vegetables = ['Pumpkin','Brinjal','Ladyfinger']


    return render(request,"index.html",context={'peoples' : peoples, 'vegetables' : vegetables})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")