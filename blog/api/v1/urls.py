from django.urls import path, include

from . import views




urlpatterns = [

    path('blog/', views.post_list, name='post_list'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    

] 