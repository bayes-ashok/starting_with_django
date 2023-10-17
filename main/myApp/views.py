from django.shortcuts import render 
# render is for template
from django.http import HttpResponse
from myApp.models import Contact
from django.contrib import messages

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
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Contact saved successfully.')    
    return render(request,"contact.html")