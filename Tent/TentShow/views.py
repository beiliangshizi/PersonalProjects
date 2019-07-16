from django.shortcuts import render

# Create your views here.


def showtents(request):
    return render(request,"showtent.html",{})

