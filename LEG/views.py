from django.shortcuts import render, redirect
from django.views import View

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/forside.html')