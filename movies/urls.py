from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns= [
    url(r'^$',views.index, name="index"),
    url(r'^',views.home, name='home')
]