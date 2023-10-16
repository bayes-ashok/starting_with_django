from django.shortcuts import render 
# render is for template
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"hi"
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")