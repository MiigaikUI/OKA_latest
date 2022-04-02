from django.shortcuts import render

# Create your views here.
from django.views import View

from main.models import About


class AboutView(View):
    def get(self, request):
        return render(request, "about.html", {"html":About.objects.all().filter(status=True)[0].html})
