from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
