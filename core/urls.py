from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),


    path(
        "about/",
        views.about,
        name="about"
    ),

    path("legal/", views.legal, name="legal"),

    path("chatbot/", views.chatbot_api, name="chatbot_api")

]