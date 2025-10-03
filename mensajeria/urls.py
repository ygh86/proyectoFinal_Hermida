from django.urls import path
from mensajeria import views

app_name = "mensajeria"

urlpatterns = [
    path("", views.chat_list, name="chat_list"),  # lista todos los chats del usuario
    path("chat/<int:chat_id>/", views.chat_detail, name="chat_detail"),  # ver un chat
    path("nuevo/<int:user_id>/", views.chat_create, name="chat_create"),  # crear chat con un usuario
]
