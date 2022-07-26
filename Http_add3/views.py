
from django.shortcuts import render


# Create your views here.
def add(request):
    return render(request,'add.html')

def exp(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+b
    return render(request,'result.html',{'result':c})


