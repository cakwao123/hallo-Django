from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def gallary(request):
    return render(request,'gallary.html')
def info(request):
    return render(request,'info.html')
def form(request):
    return render(request,'form.html')
def login(request):
    return render(request,"login.html")
def registration(request):
    return render(request,"registration.html")