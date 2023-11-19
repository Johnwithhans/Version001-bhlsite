from django.urls import path
from . import views





app_name = "bhlwebapp"


urlpatterns = [
    path('', views.index_view, name="index"),
    path('make_appointment/', views.make_appointment, name="make_appointment"),
    path('contact_us/', views.contact_us, name='contact_us'),

]