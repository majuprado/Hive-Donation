from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "app/index.html")
def sobre(request):
    return render(request, "app/sobe.html")
def equipe(request):
    return render(request, "app/equipe.html")

