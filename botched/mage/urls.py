from django.conf.urls import url
from . import views

#TODO dodac base.html + ogarnac bootstrapa
urlpatterns = [
    #url(r'^',),

    #/mage/characters
    url(r'^characters/$', views.BaseListView.as_view(), name="base-list")

]
