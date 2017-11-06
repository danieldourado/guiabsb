from django.shortcuts import render
from .models import *
import string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import AnuncioCreateForm


class AnuncioListView(ListView):
    model = Anuncio


class AnuncioCustomListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']

        slugCidade      = checkIfThereIsString(Cidade,slug)
        slugTransacao   = checkIfThereIsString(Transacao,slug)
        slugTipo        = checkIfThereIsString(Tipo,slug)
        slugQuarto      = checkIfThereIsString(Quarto,slug)
        slugBanheiro    = checkIfThereIsString(Banheiro,slug)
        slugVaga        = checkIfThereIsString(Vaga,slug)

        return Anuncio.objects.filter(cidade__slug__icontains=slugCidade,
                                    transacao__slug__icontains=slugTransacao,
                                    tipo__slug__icontains=slugTipo,
                                    quartos__slug__icontains=slugQuarto,
                                    banheiros__slug__icontains=slugBanheiro,
                                    vagas__slug__icontains=slugVaga,
                                    )


def checkIfThereIsString(model, slug):
    objects = model.objects.all()
    for obj in objects:
        if obj.slug in slug:
            return obj.slug
    return ''



class AnuncioDetailView(DetailView):
     def get_queryset(self):
        return Anuncio.objects.all()

class AnuncioCreateView(LoginRequiredMixin, CreateView):
    form_class = AnuncioCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/anuncios/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AnuncioCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(AnuncioCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Adicionar anúncio'
        return context


class AnuncioUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AnuncioCreateForm
    login_url = '/login/'
    template_name = 'imoveis/detail-update.html'
    #success_url = "/anuncios/"

    def get_context_data(self, *args, **kwargs):
        context = super(AnuncioUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = 'Atualizar Anuncio: {name}'
        return context

    def get_queryset(self):
        return Anuncio.objects.all()












# Create your views here.
def detail(request, slug):
    name = ''
    name += checkIfThereIsString(Cidade,slug)
    name += checkIfThereIsString(Transacao,slug)
    name += checkIfThereIsString(Tipo,slug)
    name += checkIfThereIsString(Quarto,slug)
    name += checkIfThereIsString(Banheiro,slug)
    name += checkIfThereIsString(Vaga,slug)
    name += checkIfThereIsString(Anuncio,slug)



    return HttpResponse(name)

