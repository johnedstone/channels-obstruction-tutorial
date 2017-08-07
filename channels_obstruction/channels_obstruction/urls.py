from django.conf.urls import url
from django.contrib import admin
from game.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', CreateUserView.as_view()),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'next_page': '/'}),

    url(r'^$', HomeView.as_view())
]
