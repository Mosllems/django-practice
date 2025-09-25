from django.urls import path, include

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('go-to-google/', views.RedirectClass.as_view(), name='google'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    # path('go-to-codingyar', views.redirect_class, name='codingyar') this is for fbv

]