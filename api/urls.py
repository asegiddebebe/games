from django.urls import path
from . import views

urlpatterns = [
	path('items/', views.getData),
	path('countries/', views.getCountries)
]