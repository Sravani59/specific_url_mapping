from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def raidu(request):
    return HttpResponse('<center><h1>Raiduuuuu</h1></center>')