from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data, name='data'),
    path('compare/', views.compare, name='compare'),
    path('uses/', views.uses, name='uses'),
    path('apps/', views.apps, name='apps'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
