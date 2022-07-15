from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<slug>', ProductDetaileView.as_view(), name='detail'),
    path('add_review', review, name='add_review'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
]
