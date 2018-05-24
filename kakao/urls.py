from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^keyboard/', views.keyboard),
    url(r'^message$', views.answer),


]
