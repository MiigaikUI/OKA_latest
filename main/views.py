import sys

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from .models import *


class MapView(View):
    def get(self, request):
        return render(request, "Map.html", {"title": "Map"})


class StaticView(View):
    def get(self, request):
        page = request.__dict__['resolver_match'].url_name.capitalize()
        page_class = getattr(sys.modules[__name__], page)
        try:
            return render(request, "Static.html",
                          {"title": page, "heading": page_class._meta.original_attrs['verbose_name_plural'],
                           "object": page_class.objects.get(status=True)})
        except:
            # TODO: refactorvc
            return HttpResponseNotFound(f'<h1 style="text-align: center;">{page} page doesn`t exists or not activated</h1>')


class SetView(View):
    def get(self, request):
        page = request.__dict__['resolver_match'].url_name.capitalize()
        page_class = getattr(sys.modules[__name__], page)
        try:
            return render(request, page + ".html",
                          {"title": page, "heading": page_class._meta.verbose_name_plural, "objects": page_class.objects.all()})
        except:
            # TODO: refactor
            return HttpResponseNotFound(f'<h1 style="text-align: center;">{page} objects doesn`t exists</h1>')


class EventView(View):
    def get(self, request, id):
        try:
            event = Event.objects.get(id=id)
            return render(request, "CurrentEvent.html", {"title": event.name, "object": event})
        except:
            # TODO: refactor
            return HttpResponseNotFound(f'<h1 style="text-align: center;">Event object with id = {id} doesn`t exists</h1>')
