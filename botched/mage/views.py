from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . import models

#TODO wyswietlic wszystkich npcow
#TODO wyswietlic szczegoly npca
#TODO formularz dodania npca
#TODO jak dodac maga? a jak technokrate?

class BaseListView(ListView):
    models = models.Base
    template_name = "mage/base_list.html"

    #def get_queryset(self):
    #    queryset = super().get_queryset()
    #    return queryset

