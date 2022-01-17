from django.shortcuts import render

from .models import Team


def demo(request):
    obj=Team.objects.all()
    return render(request ,"index.html",{'result':obj})
