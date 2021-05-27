from django.conf.urls import url
from . import views
from django.contrib import admin
urlpatterns = [
    url(r'^persons/$', views.persons, name='persons'),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]