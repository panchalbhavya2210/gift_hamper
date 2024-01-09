from django.shortcuts import render

# Create your views here.

def viewPage(request):
    return render(request, "index.html")