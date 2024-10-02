from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from . import views

app_name ='clientapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('artists/', views.artists, name='artists'),
    path('songs/', views.songs, name='songs'),
    path('contact/', views.contact, name='contact'),
    path('artists_details/<str:pk>/', views.artist_details, name='artists_details'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
