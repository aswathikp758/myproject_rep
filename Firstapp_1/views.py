from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

# return HttpResponse("<h1>Hello world</h1>")
"""in this case html code applied.but a complete webpage this is not possible,So we are using 
DTL(Django Template Language)"""

