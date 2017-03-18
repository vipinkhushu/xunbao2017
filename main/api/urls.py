from django.conf.urls import url,include
from .views import QueDetailView,check,QueDetail,check1,ranklist

urlpatterns = [
    url(r'^users/(?P<name>[\w\-]+)/que/(?P<pk>[\w\-]+)/$',QueDetailView.as_view(),name='index'),
    url(r'^home/$',QueDetail.as_view(),name='home'),
    url(r'^users/(?P<pk>[\w\-]+)/ans/(?P<ans>[\w\-]+)/$',check1.as_view(),name='check1'),
    url(r'^checking/$',check.as_view(),name="check"),
    url(r'^ranklist/$',ranklist.as_view(),name="ranklist"),
]


# url=   127.0.0.1:8000/api/home/   
#  url = 127.0.0.1:8000/api/checking 
#  url = 127.0.0.1:8000/api/ranklist/