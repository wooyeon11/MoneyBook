from django.conf.urls import include, url
from django.contrib import admin



 urlpatterns = [
 url(r'^kakao/', include('kakao.urls')),
 url(r'^admin/', admin.site.urls),
]
