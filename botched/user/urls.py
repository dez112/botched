from django.conf.urls import url
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
        #user/signup
        url(r'^signup/$', user_views.signup, name='signup'),

        # user/login
        url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),

        # user/logout
        url(r'^logout/$', auth_views.logout, {'template_name': 'users/logged_out.html'}, name='logout'),

]