from django.urls import path
from . import views

app_name = "userprofile"

urlpatterns = [
    path('<int:user_id>/', views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
