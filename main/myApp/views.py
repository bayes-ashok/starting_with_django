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
    return HttpResponse("about page")

def services(request):
    return HttpResponse("services page")

def contact(request):
    return HttpResponse("contact page")