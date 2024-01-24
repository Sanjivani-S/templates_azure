from django.conf.urls import include
from app_templates import views
from django.urls import path

## template tagging

app_name = 'app_templates'

urlpatterns = [
    path ('other/', views.other, name='other'),
    path('relative/',views.relative, name = 'relative'),
    path('home/',views.home, name = 'home'),
    path('details/',views.details, name = 'details'),
]
