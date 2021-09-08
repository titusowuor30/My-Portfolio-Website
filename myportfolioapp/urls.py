from django.urls import path,include
from .views import *

urlpatterns = [
   path('',home,name='home'),
    path('send/message/', ContactView, name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('leavemessage/',LeaveMessage,name='leavemessage'),
]