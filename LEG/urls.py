from django.urls import path
from . import views
from .views import Forside, AView, BView, CView, DView, EView

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('a/', AView.as_view(), name='a'),
  path('b/', BView.as_view(), name='b'),
  path('c/', CView.as_view(), name='c'),
  path('d/', DView.as_view(), name='d'),
  path('e/', EView.as_view(), name='e'),
]