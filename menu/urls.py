from django.urls import path
from .views import menuView

urlpatterns = [
    path('',menuView,name = 'home')
]
