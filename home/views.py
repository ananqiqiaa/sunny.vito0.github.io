from django.shortcuts import render
from .models import award
# Create your views here.
def home(request):
    awards = award.objects.all()
    return render(request,'home.html',{'active_menu':'home',
        'sub_menu':'home',
                  'awards': awards, })