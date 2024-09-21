from django.urls import path
from .import views

# Url config
urlpatterns = [
    path('', views.StaffLogin.as_view(), name="login"),
    path('auth/index.html', views.index, name="Index"),
]
