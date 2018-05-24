from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^keyboard/', views.keyboard),
    url(r'^message$', views.answer),
    url(r'^insert_data$', views.insert_data),
    url(r'^update$', views.update),
    url(r'^remove$', views.remove),
    url(r'^get_data$', views.get_data),

]
