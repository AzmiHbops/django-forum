from django.urls import path
from Comment import views

app_name = "comment"
urlpatterns = [
    path('<int:pk>/replies', views.replies, name="replies"),
    path('<parent>-new/<parent_id>/', views.create, name="create"),
    path('<int:pk>/delete/', views.delete, name="delete")
]