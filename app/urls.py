from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name='home'),
    path("about", about, name='about'),
    path("shop", shop, name='shop'),
    path("contact", contact, name='contact'),
    path("detail", shopDetail, name='shopDetail'),
]
