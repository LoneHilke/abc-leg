from django.shortcuts import render, redirect
from django.views import View
from .models import A, B, C, D, E

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/forside.html')
    
class AView(View):
    def get(self, request, *args, **kwargs):
        a = A.objects.all()
        context = {
            'a': a
        }
        
        return render(request, 'leg/a.html',context) 
    
class BView(View):
    def get(self, request, *args, **kwargs):
        b = B.objects.all()
        context = {
            'b': b
        }
        return render(request, 'leg/b.html', context)
    
class CView(View):
    def get(self, request, *args, **kwargs):
        c = C.objects.all()
        context = {
            'c': c
        }
        return render(request, 'leg/c.html', context)
    
class DView(View):
    def get(self, request, *args, **kwargs):
        d = D.objects.all()
        context = {
            'd': d
        }
        return render(request, 'leg/d.html', context)
    
class EView(View):
    def get(self, request, *args, **kwargs):
        e = E.objects.all()
        context = {
            'e': e
        }
        return render(request, 'leg/e.html', context)

       