from django.urls import path
from advert import views

app_name = "advert"
urlpatterns = [
    path('advert/', views.advert, name="advert"),
]