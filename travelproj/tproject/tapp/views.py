from django.shortcuts import render
from .models import place,team
# Create your views here.
def demo(request):
   obj=place.objects.all()
   return render(request,"index.html",{'result':obj})

def demo1(request):
   obj1 = team.objects.all()
   return render(request, "index.html", {'results': obj1})
