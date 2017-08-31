from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.forms.models import model_to_dict
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


class BaseDetailView(View): #TODO change to case    
    def get(self, request, pk):
        character = models.Base.objects.get(pk=pk)
        attr_all = models.Attributes.objects.all().filter(name=character)
        abil_all = models.Abilities.objects.all().filter(name=character)
        spheres_get = models.Spheres.objects.filter(name=character)
        techspheres_get = models.TechnocracySpheres.objects.filter(name=character)

        if (attr_all.exists()) and (abil_all.exists()):
            attributes = attr_all
            abilities = abil_all
            if character.is_technocrat:
                techspheres = techspheres_get
                return render(request, 'mage/base_detail__abat_m.html', {'object': character,
                                                                         'attr': attributes,
                                                                         'abili': abilities,
                                                                         'spheres': techspheres})
            elif character.is_mage:
                spheres = spheres_get
                return render(request, 'mage/base_detail_abat_m.html', {'object': character,
                                                                        'attr': attributes,
                                                                        'abili': abilities,
                                                                        'spheres': spheres})

            return render(request, 'mage/base_detail_abat.html', {'object': character,
                                                                'attr': attributes,
                                                                'abili': abilities})

        elif not(attr_all.exists()) and (abil_all.exists()):
            abilities = abil_all
            if character.is_technocrat:
                techspheres = techspheres_get
                return render(request, 'mage/base_detail_ab_m.html', {'object': character,
                                                                      'abili': abilities,
                                                                      'spheres': techspheres})

            elif character.is_mage:
                spheres = spheres_get
                return render(request, 'mage/base_detail_ab_m.html', {'object': character,
                                                                      'abili': abilities,
                                                                      'spheres': spheres})

            return render(request, 'mage/base_detail_ab.html', {'object': character, 'abili': abilities})

        elif (attr_all.exists()) and not(abil_all.exists()):
            attributes = attr_all

            if character.is_technocrat:
                techspheres = techspheres_get
                return render(request, 'mage/base_detail_at_m.html', {'object': character,
                                                                      'attr': attributes,
                                                                      'spheres': techspheres})

            elif character.is_mage:
                spheres = spheres_get
                return render(request, 'mage/base_detail_at_m.html', {'object': character,
                                                                      'attr': attributes,
                                                                      'spheres': spheres})

            return render(request, 'mage/base_detail_at.html', {'object': character, 'attr': attributes})

        elif character.is_technocrat:
                techspheres = techspheres_get
                return render(request, 'mage/base_detail_m.html',
                              {'object': character, 'spheres': techspheres})

        elif character.is_mage: #TODO nie dziala
            spheres = spheres_get
            return render(request, 'mage/base_detail_m.html',
                          {'object': character, 'spheres': spheres})

        else:
            return render(request, 'mage/base_detail.html', {'object': character})


class BaseCreateView(CreateView):
    model = models.Base
    fields = ['player', 'name', 'nature', 'demenor', 'willpower', 'traits', 'backgrounds', 'is_technocrat',
              'is_mage', 'is_enemy', 'is_player_character', '']
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
class SpheresListView(ListView):
    model = models.Spheres
    template_name = "mage/generic_list.html"

    #def get_queryset(self): #warning TODO get_queryset

    #def get_context_data(self, **kwargs): #warning TODO get_context_data


class SpheresDetailView(DetailView):
    model = models.Spheres


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
class TechnocracySpheresListView(ListView):
    model = models.TechnocracySpheres
    template_name = "mage/generic_list.html"

    #def get_queryset(self): #warning TODO get_queryset

    #def get_context_data(self, **kwargs): #warning TODO get_context_data


class TechnocracySpheresDetailView(DetailView):
    model = models.TechnocracySpheres


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



