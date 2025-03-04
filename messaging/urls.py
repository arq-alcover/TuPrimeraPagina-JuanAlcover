from django.urls import path
from .views import message_list, send_message

app_name = "messaging"  
urlpatterns = [
    path("", message_list, name="message_list"),  
    path("new/", send_message, name="send_message"),
]
