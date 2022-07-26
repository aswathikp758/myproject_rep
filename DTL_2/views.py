from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')   #statically print data

def home1(request):
    return render(request,'home.html',{'name':'hi'})   #dynamically print data

def bgcolor(request):
    return render(request,'bg_color.html',{'name':'hi'})   #dynamically print data
