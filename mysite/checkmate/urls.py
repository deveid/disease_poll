from django.conf.urls import url

from django.urls import path,re_path
from . import views

urlpatterns = [
                url(r'^$', views.CreateMyModelView.as_view(), name='name'),
                url(r'^results$', views.MyModelListView.as_view(), name='result'),
]