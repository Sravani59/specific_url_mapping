from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def raidu(request):
    return HttpResponse('<center><h1>Raidu Two</h1></center>')