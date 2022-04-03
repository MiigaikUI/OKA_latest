from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View

from main.models import About

class AboutView(View):
    def get(self, request):
        try:
            return render(request, "about.html", {"html":About.objects.all().filter(status=True)[0].html})
        except:
            #TODO: refactor
            return HttpResponseNotFound('<h1 style="text-align: center;">About page doesn`t exists or not activated</h1>')