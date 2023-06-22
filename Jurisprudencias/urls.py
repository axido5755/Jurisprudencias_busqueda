from django.urls import path
from .views import list_jurisprudencias, create_jurisprudencias

urlpatterns = [
    path('lista/',list_jurisprudencias, name='list_jurisprudencias'),
    path('new/', create_jurisprudencias, name='create_jurisprudencias')    
]