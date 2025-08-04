from django.shortcuts import render, redirect
from django.views import View
from .models import A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet
from .forms import GætForm, EkstraForm
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
        a = random.choice(A.objects.all())
        b = random.choice(B.objects.all())
        c = random.choice(C.objects.all())
        d = random.choice(D.objects.all())
        e = random.choice(E.objects.all())
        f = random.choice(F.objects.all())
        g = random.choice(G.objects.all())
        h = random.choice(H.objects.all())
        form = GætForm()
        return render(request, 'leg/gaet.html', {
            'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g':g, 'h':h,
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = GætForm(request.POST)
        resultat = None
        aktiv_model = None
        aktiv_id = None

    # Find ud af hvilken form der blev sendt
        if 'a_id' in request.POST:
            aktiv_model = 'a'
            aktiv_id = request.POST.get('a_id')
            obj = A.objects.get(id=aktiv_id)
        elif 'b_id' in request.POST:
            aktiv_model = 'b'
            aktiv_id = request.POST.get('b_id')
            obj = B.objects.get(id=aktiv_id)
        elif 'c_id' in request.POST:
            aktiv_model = 'c'
            aktiv_id = request.POST.get('c_id')
            obj = C.objects.get(id=aktiv_id)
        elif 'd_id' in request.POST:
            aktiv_model = 'd'
            aktiv_id = request.POST.get('d_id')
            obj = D.objects.get(id=aktiv_id)
        elif 'e_id' in request.POST:
            aktiv_model = 'e'
            aktiv_id = request.POST.get('e_id')
            obj = E.objects.get(id=aktiv_id)
        elif 'f_id' in request.POST:
            aktiv_model = 'f'
            aktiv_id = request.POST.get('f_id')
            obj = F.objects.get(id=aktiv_id)
        elif 'g_id' in request.POST:
            aktiv_model = 'g'
            aktiv_id = request.POST.get('g_id')
            obj = G.objects.get(id=aktiv_id)
        elif 'h_id' in request.POST:
            aktiv_model = 'h'
            aktiv_id = request.POST.get('h_id')
            obj = H.objects.get(id=aktiv_id)
        if 'i_id' in request.POST:
            aktiv_model = 'i'
            aktiv_id = request.POST.get('i_id')
            obj = I.objects.get(id=aktiv_id)
        elif 'j_id' in request.POST:
            aktiv_model = 'j'
            aktiv_id = request.POST.get('j_id')
            obj = J.objects.get(id=aktiv_id)
        elif 'k_id' in request.POST:
            aktiv_model = 'k'
            aktiv_id = request.POST.get('k_id')
            obj = K.objects.get(id=aktiv_id)
        elif 'l_id' in request.POST:
            aktiv_model = 'l'
            aktiv_id = request.POST.get('l_id')
            obj = L.objects.get(id=aktiv_id)
        elif 'm_id' in request.POST:
            aktiv_model = 'm'
            aktiv_id = request.POST.get('m_id')
            obj = M.objects.get(id=aktiv_id)
        elif 'n_id' in request.POST:
            aktiv_model = 'n'
            aktiv_id = request.POST.get('n_id')
            obj = N.objects.get(id=aktiv_id)
        elif 'o_id' in request.POST:
            aktiv_model = 'o'
            aktiv_id = request.POST.get('o_id')
            obj = O.objects.get(id=aktiv_id)
        elif 'p_id' in request.POST:
            aktiv_model = 'p'
            aktiv_id = request.POST.get('p_id')
            obj = P.objects.get(id=aktiv_id)
        else:
            obj = None

    # Vurder gæt
        if obj and form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            korrekt = obj.ord.strip().lower()

            if gæt == korrekt:
                resultat = "✅ Korrekt!"
                # Vælg et nyt billede efter korrekt svar
                if aktiv_model == 'a':
                    obj = random.choice(A.objects.all())
                elif aktiv_model == 'b':
                    obj = random.choice(B.objects.all())
                elif aktiv_model == 'c':
                    obj = random.choice(C.objects.all())
                elif aktiv_model == 'd':
                    obj = random.choice(D.objects.all())
                elif aktiv_model == 'e':
                    obj = random.choice(E.objects.all())
                elif aktiv_model == 'f':
                    obj = random.choice(F.objects.all())
                elif aktiv_model == 'g':
                    obj = random.choice(G.objects.all())
                elif aktiv_model == 'h':
                    obj = random.choice(H.objects.all())
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {obj.ord}"

        # Alt indhold
            context = {
                'a': random.choice(A.objects.all()),
                'b': random.choice(B.objects.all()),
                'c': random.choice(C.objects.all()),
                'd': random.choice(D.objects.all()),
                'e': random.choice(E.objects.all()),
                'f': random.choice(F.objects.all()),
                'g': random.choice(G.objects.all()),
                'h': random.choice(H.objects.all()),
                'form': form,
                'resultat': resultat,
                'aktiv_model': aktiv_model,
                'aktiv_id': int(aktiv_id) if aktiv_id else None,
            }

            return render(request, 'leg/gaet.html', context)
        
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/Info.html')
    
class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        context = {
            'form':form
        }
        return render(request, 'leg/tilføj.html', context)



"""class GætView(View):
    def get(self, request, *args, **kwargs):
        a = random.choice(A.objects.all())  # Vælg et tilfældigt billede
        b = random.choice(B.objects.all())  # Vælg et tilfældigt billede
        c = random.choice(C.objects.all())  # Vælg et tilfældigt billede
        d = random.choice(D.objects.all())  # Vælg et tilfældigt billede
        e = random.choice(E.objects.all())  # Vælg et tilfældigt billede
        f = random.choice(F.objects.all())  # Vælg et tilfældigt billede
        form = GætForm()
        return render(request, 'leg/gaet.html', {'a': a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'form': form})

    def post(self, request, *args, **kwargs):
        a_id = request.POST.get('a_id') 
        a = A.objects.get(id=a_id)
        form = GætForm(request.POST)
        b_id = request.POST.get('b_id')
        b = B.objects.get(id=b_id)
        form = GætForm(request.POST)
        c_id = request.POST.get('c_id')
        c = C.objects.get(id=c_id)
        form = GætForm(request.POST)
        d_id = request.POST.get('d_id')
        d = D.objects.get(id=d_id)
        form = GætForm(request.POST)
        e_id = request.POST.get('e_id')
        e = E.objects.get(id=e_id)
        form = GætForm(request.POST)
        f_id = request.POST.get('f_id')
        f = F.objects.get(id=f_id)
        form = GætForm(request.POST)
        resultat = None

        context = {
            'a': a, 
            'b':b, 
            'c':c,
            'd':d,
            'e':e, 
            'f':f,
        }

        if form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            korrekt = a.ord.strip().lower()
            korrekt = b.ord.strip().lower()
            korrekt = c.ord.strip().lower()
            korrekt = d.ord.strip().lower()
            korrekt = e.ord.strip().lower()
            korrekt = f.ord.strip().lower()
            
            if gæt == korrekt:
                resultat = "✅ Korrekt!"
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {a.ord},{b.ord},{c.ord},{d.ord},{e.ord},{f.ord}"

        return render(request, 'leg/gaet.html', context, { 'form': form, 'resultat': resultat})

    def post(self, request, *args, **kwargs):
        b = random.choice(B.objects.all())  # Vælg et tilfældigt billede
        b_id = request.POST.get('b_id')
        b = B.objects.get(id=b_id)
        form = GætForm(request.POST)
        resultat = None

        if form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            
            korrekt = b.ord.strip().lower()
            if gæt == korrekt:
                resultat = "✅ Korrekt!"
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {b.ord}"

        return render(request, 'leg/gaet.html', {'b':b, 'form': form, 'resultat': resultat})

    def get(self, request, *args, **kwargs):
        alfabet = Alfabet.objects.filter()  # fx udvalgte billeder fra session eller alfabet
        return render(request, 'leg/gaet.html', {'alfabet': alfabet})

    def post(self, request, *args, **kwargs):
        alfabet_id = request.POST.get('alfabet_id')
        alfabet = Alfabet.objects.get(id=alfabet_id)
        gæt = request.POST.get('gæt', '').strip().lower()
        korrekt = alfabet.ord.strip().lower()
        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert. Det rigtige svar er: {korrekt}"

        alfabet = Alfabet.objects.all()
        feedback = {int(alfabet_id): resultat}  # dict med ID som nøgle

        return render(request, 'leg/gaet.html', {
            'alfabet': alfabet,
            'feedback': feedback
        })
    
    def get(self, request, *args, **kwargs):
        a = random.choice(A.objects.all())  # Vælg et tilfældigt 
        b = random.choice(B.objects.all())  # Vælg et tilfældigt billede
        form = GætForm()
        return render(request, 'leg/gaet.html', {
            'a': a, 
            'b':b,
            'form': form
            })"""

    

       