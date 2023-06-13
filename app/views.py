from django.shortcuts import render

# Create your views here.

def loop(request):
    return render(request,'loop.html')
