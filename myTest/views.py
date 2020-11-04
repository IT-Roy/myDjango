from django.shortcuts import render

# Create your views here.

def myTest(request):
    return render(request, 'test.html')