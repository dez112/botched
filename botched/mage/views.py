from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from . import models

#TODO wyswietlic szczegoly npca + dodatki jezeli są dodane --> if xx is true(get object)
#TODO formularz dodania npca
#TODO jak dodac maga? a jak technokrate? -->javascript
#TODO base detail - dodac szczegoly postaci

####### Chronicle related views
class ChronicleListView(ListView):
    model = models.Chronicle
    template_name ='mage/chronicle_list.html'


class ChronicleWelcomeView(TemplateView):
    template_name = "mage/chronicle_welcome.html"


class ChronicleCreteView(CreateView):
    model = models.Chronicle
    template_name = "mage/generic_form.html"


####### Characters related views
class BaseListView(ListView):
    model = models.Base
    template_name = "mage/base_list.html"

    #def get_queryset(self): #warning TODO get_queryset

    #def get_context_data(self, **kwargs): #warning TODO get_context_data


class BaseDetailView(DetailView):
    model = models.Base


class BaseCreateView(CreateView):
    model = models.Base
    fields = '__all__'
    template_name = "mage/generic_form.html"


class BaseUpdateView(UpdateView):
    model = models.Base
    fields = '__all__'
    template_name = "mage/generic_form.html"

#class


class BaseDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Base


####### Attributes related views
class AttributesListView(ListView):
    model = models.Attributes
    template_name = "mage/base_list.html"

    #def get_queryset(self): #warning TODO get_queryset

    #def get_context_data(self, **kwargs): #warning TODO get_context_data


class AttributesDetailView(DetailView):
    model = models.Attributes


class AttributesCreateView(CreateView):
    model = models.Attributes
    fields = '__all__'
    template_name = "mage/generic_form.html"


class AttributesUpdateView(UpdateView):
    model = models.Attributes
    fields = '__all__'
    template_name = "mage/generic_form.html"


class AttributesDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Attributes


####### Abilities related views






####### Mage related views





####### Technocrat related views




