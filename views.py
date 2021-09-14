from django.shortcuts import render

# Create your views here.


def dylan(request):
    return render(request, 'dp/dylan.html')