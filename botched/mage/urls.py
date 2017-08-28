from django.conf.urls import url
from . import views

#TODO dodac base.html + ogarnac bootstrapa
urlpatterns = [
    #url(r'^',),

    #/mage/characters
    url(r'^characters/$', views.BaseListView.as_view(), name="base-list"),

    #mage/characters/pk
    url(r'^characters/(?P<pk>(\d)+)', views.BaseDetailView.as_view(), name="base-detail-view"),

    #/mage/characters/add-character
    url(r'^characters/add-character', views.BaseCreateView.as_view(), name="base-create-view"),

]
