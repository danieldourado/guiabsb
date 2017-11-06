from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from imoveis.views import *

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^imoveis/', include('imoveis.urls', namespace='imoveis')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^imoveis/(?P<slug>[\w-]+)/$', detail, name='about'),
]