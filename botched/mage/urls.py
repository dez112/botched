from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#TODO dodac base.html + ogarnac bootstrapa
urlpatterns = [
    #url(r'^',),

    #/mage/chronicle
    url(r'^chronicle/$', views.ChronicleListView.as_view(), name="chronicle-list"),

    #mage/chronicle/pk
    url(r'^chronicle/(?P<pk>(\d)+)', views.ChronicleWelcomeView.as_view(), name='chronicle-welcome'),

    #mage/chronicle/add-new
    url(r'^chronicle/add-new', views.ChronicleCreteView.as_view(), name='chronicle-create-view'),

    #/mage/characters
    url(r'^characters/$', views.BaseListView.as_view(), name="base-list"),

    #mage/characters/pk
    url(r'^characters/(?P<pk>(\d)+)', views.BaseDetailView.as_view(), name="base-detail-view"),

    #/mage/characters/add-character
    url(r'^characters/add-character', views.BaseCreateView.as_view(), name="base-create-view"),

    #/mage/characters/delete-character/pk
    url(r'^characters/delete-character/(?P<pk>(\d)+)', views.BaseDeleteView.as_view(), name="base-delete-view"),

    #/mage/characters/edit-character/pk
    url(r'^characters/edit-character/(?P<pk>(\d)+)', views.BaseUpdateView.as_view(), name="base-update-view"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
