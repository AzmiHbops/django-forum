from django.urls import path
from Post import views


app_name = "post"
urlpatterns = [
    path('', views.home, name="home"),
    path('<tag_slug>/', views.home, name="home"),
    path('<int:pk>/<slug:slug>/detail/', views.detail, name="detail"),
    path('213/2444376611987366/', views.profile, name="profile"),
    path('post/new/', views.create, name="create"),
    path('<int:pk>/<slug:slug>/edit/', views.edit, name="edit"),
    path('<int:pk>/<slug:slug>/delete/', views.delete, name="delete")
]
