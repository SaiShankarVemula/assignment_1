from django.shortcuts import render

# Create your views here.
def gen1(request):
    return render(request,'gen1.html')

def spec1(request):
    return render(request,'spec1.html')