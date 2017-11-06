from django.conf.urls import url


from .views import (
    AnuncioListView,
    AnuncioDetailView,
    AnuncioCreateView,
    AnuncioUpdateView,
    AnuncioCustomListView,


)
urlpatterns = [
    url(r'^create/$',  AnuncioCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', AnuncioCustomListView.as_view(), name='custom-list'),
    url(r'^(?P<slug>[\w-]+)/detalhes/$', AnuncioUpdateView.as_view(), name='detail'),
    url(r'$', AnuncioListView.as_view(), name='list'),
]