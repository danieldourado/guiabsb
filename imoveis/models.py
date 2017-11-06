from django.db import models
from guiabsb.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .validators import validate_category
from django.core.urlresolvers import reverse
from django.db.models import Q


User = settings.AUTH_USER_MODEL


class AnuncioQuerySet(models.query.QuerySet):
    def search(self, query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(cidade__icontains=query)|
                Q(transacao__iexact=query)|
                Q(tipo__icontains=query)|
                Q(quartos__iexact=query)
                ).distinct()
        return self


class AnuncioManager(models.Manager):
    def get_queryset(self):
        return AnuncioQuerySet(self.model, using=self._db)

    def search(self, query): #RestaurantLocation.objects.search()
        return self.get_queryset().search(query)


# Create your models here.
class Cidade(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Transacao(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Tipo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Quarto(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Banheiro(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Vaga(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

class Anuncio(models.Model):
    name = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade)
    transacao = models.ForeignKey(Transacao)
    tipo = models.ForeignKey(Tipo)
    quartos = models.ForeignKey(Quarto)
    banheiros = models.ForeignKey(Banheiro)
    vagas = models.ForeignKey(Vaga)
    slug = models.CharField(max_length=200, null=True, blank=True)

    objects = AnuncioManager()

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}"
        return reverse('imoveis:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name




def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Cidade)
pre_save.connect(rl_pre_save_receiver, sender=Transacao)
pre_save.connect(rl_pre_save_receiver, sender=Tipo)
pre_save.connect(rl_pre_save_receiver, sender=Quarto)
pre_save.connect(rl_pre_save_receiver, sender=Banheiro)
pre_save.connect(rl_pre_save_receiver, sender=Vaga)
pre_save.connect(rl_pre_save_receiver, sender=Anuncio)