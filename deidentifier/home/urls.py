from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Url config
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('help/', views.help)
]

urlpatterns += staticfiles_urlpatterns()