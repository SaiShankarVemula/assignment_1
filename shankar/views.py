from django.shortcuts import render

# Create your views here.
def gen2(request):
    return render(request,'gen2.html')

def spec2(request):
    return render(request,'spec2.html')