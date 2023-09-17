from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.user_detail import UserDetailViewSet

router = DefaultRouter()
router.register(
    r"user-detail",
    UserDetailViewSet,
    basename="user-detail",
)

urlpatterns = [
    path(
        "cab/",
        include((router.urls, "cab"), namespace="cab"),
    ),
]
