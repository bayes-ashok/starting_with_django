from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def counter(request):
    words=request.POST['words']
    number=len(words.split())
    return render(request,"counter.html",{"number":number})