from django.conf.urls import url
from django.urls import path, include
from api.views import PostViewSet, GroupAPIList, GroupAPIDetail, CommentAPIList, CommentAPIDetail, TokenCreateView, TokenDestroyView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('api-token-auth/logout/', TokenDestroyView.as_view()),
    path('api-token-auth/', TokenCreateView.as_view()),
    path('', include(router.urls)),
    path('groups/', GroupAPIList.as_view()),
    path('groups/<int:group_id>/', GroupAPIDetail.as_view()),
    path('posts/<int:post_id>/comments/', CommentAPIList.as_view()),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentAPIDetail.as_view()),
]
