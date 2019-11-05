from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^client/',views.client_index,name='client_index'),
    url(r'^profile/',views.client_profile,name='client_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)