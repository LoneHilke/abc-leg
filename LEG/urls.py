from django.urls import path
from . import views
from .views import Forside, AView, BView

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('a/', AView.as_view(), name='a'),
  path('b/', BView.as_view(), name='b'),
]