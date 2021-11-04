""" from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from chat import views as chat_view

urlpatterns = [
    path('', chat_view.index),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
 """
