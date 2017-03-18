from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^(?P<pk>(\d+)+)/$',views.index,name='index'),
    url(r'^(?P<pk>(\d+))/ans/(?P<ans>[\w\-]+)/$',views.check,name='check'),
    url(r'^ranks/$',views.ranks,name='ranks'),
]