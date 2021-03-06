from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #/mage/chronicle
    url(r'^chronicle/$', views.ChronicleListView.as_view(), name="chronicle-list"),

    #mage/chronicle/pk
    url(r'^chronicle/(?P<pk>(\d)+)', views.ChronicleWelcomeView.as_view(), name='chronicle-welcome'),

    #mage/chronicle/add-new
    url(r'^chronicle/add-new', views.ChronicleCreteView.as_view(), name='chronicle-create-view'),

############################################### CHARACTERS
    #mage/chronicle/characters/pk
    url(r'^chronicle/characters/(?P<pk>(\d)+)$', views.BaseListView.as_view(), name="base-list"),

    #mage/characters/pk
    url(r'^characters/(?P<pk>(\d)+)', views.BaseDetailView.as_view(), name="base-detail-view"),

    #/mage/characters/add-character
    url(r'^characters/add-character', views.BaseCreateView.as_view(), name="base-create-view"),

    #/mage/characters/delete-character/pk
    url(r'^characters/delete-character/(?P<pk>(\d)+)', views.BaseDeleteView.as_view(), name="base-delete-view"),

    #/mage/characters/edit-character/pk
    url(r'^characters/edit-character/(?P<pk>(\d)+)', views.BaseUpdateView.as_view(), name="base-update-view"),

############################################### ATTRIBUTES
    #/mage/characters/attributes/add-attribute
    url(r'^characters/attributes/add-attribute', views.AttributesCreateView.as_view(),
        name="attributes-create-view"),

    #/mage/characters/attributes/delete-attribute/pk
    url(r'^characters/attributes/delete-attribute/(?P<pk>(\d)+)', views.AttributesDeleteView.as_view(),
        name="attributes-delete-view"),

    #/mage/characters/attributes/edit-attribute/pk
    url(r'^characters/attributes/edit-attribute/(?P<pk>(\d)+)', views.AttributesUpdateView.as_view(),
        name="attributes-update-view"),

############################################### ABILITIES
    #/mage/characters/add-character
    url(r'^characters/abilities/add-abilities', views.AbilitiesCreateView.as_view(),
        name="abilities-create-view"),

    #/mage/characters/delete-character/pk
    url(r'^characters/abilities/delete-abilities/(?P<pk>(\d)+)', views.AbilitiesDeleteView.as_view(),
        name="abilities-delete-view"),

    #/mage/characters/edit-character/pk
    url(r'^characters/abilities/edit-abilities/(?P<pk>(\d)+)', views.AbilitiesUpdateView.as_view(),
        name="abilities-update-view"),

############################################### SPHERES
    #/mage/characters/add-sphere
    url(r'^characters/add-sphere', views.SpheresCreateView.as_view(), name="spheres-create-view"),

    #/mage/characters/delete-character/pk
    url(r'^characters/edit-sphere/(?P<pk>(\d)+)', views.SpheresUpdateView.as_view(), name="spheres-update-view"),

    #/mage/characters/edit-character/pk
    url(r'^characters/delete-sphere/(?P<pk>(\d)+)', views.SpheresDeleteView.as_view(), name="spheres-delete-view"),

############################################### TECHNOCRACY SPHERES
    #/mage/characters/add-techsphere
    url(r'^characters/add-techsphere', views.TechnocracySpheresCreateView.as_view(), name="techsphere-create-view"),

    #/mage/characters/delete-character/pk
    url(r'^characters/delete-techsphere/(?P<pk>(\d)+)', views.TechnocracySpheresUpdateView.as_view(), name="techsphere-delete-view"),

    #/mage/characters/edit-character/pk
    url(r'^characters/edit-techsphere/(?P<pk>(\d)+)', views.TechnocracySpheresDeleteView.as_view(), name="techsphere-update-view"),

############################################### STUFF
    #/mage/characters/find-npc
    url(r'^characters/find-npc', views.NpcSearchView.as_view(), name="find-npc"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
