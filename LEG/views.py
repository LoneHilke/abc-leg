from django.shortcuts import render, redirect
from django.views import View
from .models import A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet
from .forms import GætForm
import random

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
    
class FView(View):
    def get(self, request, *args, **kwargs):
        f = F.objects.all()
        context = {
            'f': f
        }
        return render(request, 'leg/f.html', context)
    
class GView(View):
    def get(self, request, *args, **kwargs):
        g = G.objects.all()
        context = {
            'g': g
        }
        return render(request, 'leg/g.html', context)
    
class HView(View):
    def get(self, request, *args, **kwargs):
        h = H.objects.all()
        context = {
            'h': h
        }
        return render(request, 'leg/h.html', context)
    
class IView(View):
    def get(self, request, *args, **kwargs):
        i = I.objects.all()
        context = {
            'i':i 
        }
        return render(request, 'leg/i.html', context)
    
class JView(View):
    def get(self, request, *args, **kwargs):
        j = J.objects.all()
        context = {
            'j': j
        }
        return render(request, 'leg/j.html', context)
    
class KView(View):
    def get(self, request, *args, **kwargs):
        k = K.objects.all()
        context = {
            'k': k
        }
        return render(request, 'leg/k.html', context)
    

    
class LView(View):
    def get(self, request, *args, **kwargs):
        l = L.objects.all()
        context = {
            'l': l
        }
        return render(request, 'leg/l.html', context)
    
class MView(View):
    def get(self, request, *args, **kwargs):
        m = M.objects.all()
        context = {
            'm': m
        }
        return render(request, 'leg/m.html', context)
    
class NView(View):
    def get(self, request, *args, **kwargs):
        n = N.objects.all()
        context = {
            'n': n
        }
        return render(request, 'leg/n.html', context)
    
class OView(View):
    def get(self, request, *args, **kwargs):
        o = O.objects.all()
        context = {
            'o': o
        }
        return render(request, 'leg/o.html', context)
    
class PView(View):
    def get(self, request, *args, **kwargs):
        p = P.objects.all()
        context = {
            'p': p
        }
        return render(request, 'leg/p.html', context)
    
class QView(View):
    def get(self, request, *args, **kwargs):
        q = Q.objects.all()
        context = {
            'q': q
        }
        return render(request, 'leg/q.html', context)
    
class RView(View):
    def get(self, request, *args, **kwargs):
        r = R.objects.all()
        context = {
            'r': r
        }
        return render(request, 'leg/r.html', context)
    
class SView(View):
    def get(self, request, *args, **kwargs):
        s = S.objects.all()
        context = {
            's': s
        }
        return render(request, 'leg/s.html', context)
    
class TView(View):
    def get(self, request, *args, **kwargs):
        t = T.objects.all()
        context = {
            't': t
        }
        return render(request, 'leg/t.html', context)
    
class UView(View):
    def get(self, request, *args, **kwargs):
        u = U.objects.all()
        context = {
            'u': u
        }
        return render(request, 'leg/u.html', context)
    
class VView(View):
    def get(self, request, *args, **kwargs):
        v = V.objects.all()
        context = {
            'v': v
        }
        return render(request, 'leg/v.html', context)
    
class WView(View):
    def get(self, request, *args, **kwargs):
        w = W.objects.all()
        context = {
            'w': w
        }
        return render(request, 'leg/w.html', context)
    
class XView(View):
    def get(self, request, *args, **kwargs):
        x = X.objects.all()
        context = {
            'x': x
        }
        return render(request, 'leg/x.html', context)
    
class YView(View):
    def get(self, request, *args, **kwargs):
        y = Y.objects.all()
        context = {
            'y': y
        }
        return render(request, 'leg/y.html', context)
    
class ZView(View):
    def get(self, request, *args, **kwargs):
        z = Z.objects.all()
        context = {
            'z': z
        }
        return render(request, 'leg/z.html', context)
    
class ÆView(View):
    def get(self, request, *args, **kwargs):
        æ = Æ.objects.all()
        context = {
            'æ': æ
        }
        return render(request, 'leg/æ.html', context)
    
class ØView(View):
    def get(self, request, *args, **kwargs):
        ø = Ø.objects.all()
        context = {
            'ø': ø
        }
        return render(request, 'leg/ø.html', context)
    
class ÅView(View):
    def get(self, request, *args, **kwargs):
        å = Å.objects.all()
        context = {
            'å': å
        }
        return render(request, 'leg/å.html', context)
    
class GætView(View):
    def get(self, request, *args, **kwargs):
        billeder = Alfabet.objects.filter(...)  # fx udvalgte billeder fra session eller alfabet
        return render(request, 'leg/tjek_tidligere.html', {'billeder': billeder})

    def post(self, request, *args, **kwargs):
        billede_id = request.POST.get('billede_id')
        billede = Alfabet.objects.get(id=billede_id)
        gæt = request.POST.get('gæt', '').strip().lower()
        korrekt = billede.ord.strip().lower()
        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert. Det rigtige svar er: {korrekt}"

        billeder = Alfabet.objects.all()
        feedback = {int(billede_id): resultat}  # dict med ID som nøgle

        return render(request, 'leg/tjek_tidligere.html', {
            'billeder': billeder,
            'feedback': feedback
        })
    """def get(self, request, *args, **kwargs):
        a = random.choice(A.objects.all())  # Vælg et tilfældigt 
        b = random.choice(B.objects.all())  # Vælg et tilfældigt billede
        form = GætForm()
        return render(request, 'leg/gaet.html', {
            'a': a, 
            'b':b,
            'form': form
            })

    def post(self, request, *args, **kwargs):
        a_id = request.POST.get('a_id')
        a = A.objects.get(id=a_id)
        b_id = request.POST.get('b_id')
        b = B.objects.get(id=b_id)
        form = GætForm(request.POST)
        resultat = None

        if form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            korrekt = a.ord.strip().lower()
            korrekt = b.ord.strip().lower()
            if gæt == korrekt:
                resultat = "✅ Korrekt!"
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {a.ord},{b.ord}"

        return render(request, 'leg/gaet.html', {'a': a, 'b':b, 'form': form, 'resultat': resultat})"""
     

       