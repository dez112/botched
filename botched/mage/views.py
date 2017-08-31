from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from . import models


####### Chronicle related views
class ChronicleListView(ListView):
    model = models.Chronicle
    template_name ='mage/chronicle_list.html'


class ChronicleWelcomeView(TemplateView):
    template_name = "mage/chronicle_welcome.html"


class ChronicleCreteView(CreateView):
    model = models.Chronicle
    template_name = "mage/generic_form.html"
    fields = '__all__'


####### Characters related views
class BaseListView(View):
     def get(self, request, pk):
        chronicle = models.Chronicle.objects.get(pk=pk)
        character = models.Base.objects.filter(chname=chronicle)

        return render(request, "mage/base_list.html",
                      {"object_list": character, "chronicle_name": chronicle.name})


class BaseDetailView(View):    
    def get(self, request, pk):
        character = models.Base.objects.get(pk=pk)
        
        #check if character has attributes
        try:
            attr_all = models.Attributes.objects.get(name=character)
        except ObjectDoesNotExist:
            attr_all = None

        # check if character has abilities
        try:
            abil_all = models.Abilities.objects.get(name=character)
        except ObjectDoesNotExist:
            abil_all = None

        # check if character has spheres
        try:
            spheres_get = models.Spheres.objects.get(name=character)
        except ObjectDoesNotExist:
            spheres_get = None

        # check if character has techspheres
        try:
            techspheres_get = models.TechnocracySpheres.objects.get(name=character)
        except ObjectDoesNotExist:
            techspheres_get = None
    
        # go to correct template    
        if (attr_all != None) and (abil_all != None):
            attributes = attr_all
            abilities = abil_all
            return render(request, 'mage/base_detail_abat.html', {'object': character,
                                                                  'spheres': spheres_get,
                                                                  'techspheres': techspheres_get, 
                                                                  'attr': attributes,
                                                                  'abili': abilities})

        elif (attr_all == None) and (abil_all != None):
            abilities = abil_all
            return render(request, 'mage/base_detail_ab.html', {'object': character,
                                                                'spheres': spheres_get,
                                                                'techspheres': techspheres_get,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'abili': abilities})

        elif (attr_all != None) and (abil_all == None):
            attributes = attr_all
            return render(request, 'mage/base_detail_at.html', {'object': character,
                                                                'spheres': spheres_get,
                                                                'techspheres': techspheres_get,
                                                                'attr': attributes})

        else:
            return render(request, 'mage/base_detail.html', {'object': character, 
                                                             'spheres': spheres_get,
                                                             'techspheres': techspheres_get})


class BaseCreateView(CreateView):
    model = models.Base
    fields = ['player', 'chname', 'name', 'nature', 'demenor', 'willpower', 'traits', 'backgrounds', 'is_technocrat',
              'is_mage', 'is_enemy', 'is_player_character', ]
    template_name = "mage/generic_form.html"


class BaseUpdateView(UpdateView):
    model = models.Base
    fields = '__all__'
    template_name = "mage/generic_form.html"

#class


class BaseDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Base


####### Attributes related views
class AttributesCreateView(CreateView):
    model = models.Attributes
    fields = ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'apperance', 'perception',
              'intelligencee', 'wits'] 
    template_name = "mage/generic_form.html"
    success_url = "mage/chronicle_welcome.html" #TODO poprawic, bo nie działa. Jak miałoby?

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.name_id = int(self.request.GET['mage'])
        obj.save()
        return render(self.request, self.success_url)


class AttributesUpdateView(UpdateView):
    model = models.Attributes
    fields = ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'apperance', 'perception',
              'intelligencee', 'wits']
    template_name = "mage/generic_form.html"


class AttributesDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Attributes


####### Abilities related views
class AbilitiesCreateView(CreateView):
    model = models.Abilities
    fields = '__all__'
    template_name = "mage/generic_form.html"
    #TODO dodac sucess url, bo dupa :(
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.name_id = int(self.request.GET['mage'])
        obj.save()
        return render(self.request, self.success_url)


class AbilitiesUpdateView(UpdateView):
    model = models.Abilities
    fields = '__all__'
    template_name = "mage/generic_form.html"


class AbilitiesDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Abilities


####### Mage related views
class SpheresCreateView(CreateView):
    model = models.Spheres
    fields = '__all__'
    template_name = "mage/generic_form.html"


class SpheresUpdateView(UpdateView):
    model = models.Spheres
    fields = '__all__'
    template_name = "mage/generic_form.html"


class SpheresDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.Spheres


####### Technocrat related views
class TechnocracySpheresCreateView(CreateView):
    model = models.TechnocracySpheres
    fields = '__all__'
    template_name = "mage/generic_form.html"


class TechnocracySpheresUpdateView(UpdateView):
    model = models.TechnocracySpheres
    fields = '__all__'
    template_name = "mage/generic_form.html"


class TechnocracySpheresDeleteView(DetailView): #TODO delete view - nie dziala :(
    model = models.TechnocracySpheres



