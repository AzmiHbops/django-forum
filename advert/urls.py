from django.urls import path
from advert import views

app_name = "advert"
urlpatterns = [
    path('advert/', views.advert, name="advert"),
    path('checkout/', views.checkout, name="ad_checkout"),
    path('checked_out/', views.checked_out, name="checked_out"),
]