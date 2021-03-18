from django.urls import path
from Comment import views

app_name = "comment"
urlpatterns = [
    path('<int:pk>/96/replies', views.replies, name="replies"),
    path('<parent>-new/<parent_id>/', views.create, name="create"),
    path('<int:pk>/14/reply/edit/', views.edit, name="edit"),
    path('<int:pk>/32/delete/', views.delete, name="delete")
]