
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',post_list, name ="post_list"),
    path('post_game/',post_game, name ="post_game"),
    path('post_script/',post_script, name ="post_script"),

    #===============URL======================================
    path('script/<int:pk>/',script,name="script"),



]
