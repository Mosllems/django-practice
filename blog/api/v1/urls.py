from django.urls import path, include

from . import views




urlpatterns = [

    path('blog/', views.post_list, name='post_list'),

] 