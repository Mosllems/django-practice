from django.urls import path, include

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('go-to-google/', views.RedirectClass.as_view(), name='google'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/create/', views.PostCreate.as_view(), name='post_create'),
    path('blog/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('blog/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('api/v1/', include('blog.api.v1.urls')),

    # path('go-to-google', views.redirect_class, name='codingyar') this is for fbv
] 