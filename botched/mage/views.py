from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . import models

#TODO wyswietlic szczegoly npca + dodatki jezeli są dodane --> if xx is true(get object)
#TODO formularz dodania npca
#TODO jak dodac maga? a jak technokrate? -->javascript

class BaseListView(ListView):
    model = models.Base
    template_name = "mage/base_list.html"

class BaseDetailView(DetailView):
    model = models.Base

class BaseCreateView(CreateView):
    model = models.Base
    fields = '__all__'
    template_name = "mage/generic_form.html"