from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ask/", views.ask_question, name="ask"),
    path("history/", views.question_history),
    path("accounts/register/", views.register, name="register"),
    path("accounts/logout/", views.logout_view, name="logout"),  
]
