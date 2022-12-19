from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('post', views.PostViewSet)
# router.register('comment', views.CommentListCreateView)

urlpatterns = [
    path('', include(router.urls)),
    path('comment/', views.CommentListCreateView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]