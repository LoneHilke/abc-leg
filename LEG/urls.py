from django.urls import path
from . import views
from .views import Forside

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
]