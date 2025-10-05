from rest_framework.routers import DefaultRouter

from . import views

app_name = "api-v1"

router = DefaultRouter()


router.register("blog", views.PostViewSet, basename="blog")
router.register("category", views.CategoryViewSet, basename="category")


urlpatterns = router.urls


# urlpatterns = [

#     # path('blog/', views.post_list, name='post_list'),
#     # path('blog/<int:pk>/', views.post_detail, name='post_detail'),

#     path('blog/', views.PostList.as_view(), name='post_list'),
#     path('blog/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

# ]
