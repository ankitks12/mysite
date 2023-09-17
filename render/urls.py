from django.urls import path, include
from rest_framework.routers import DefaultRouter

from render.views import views


from render.views.user_detail import UserDetailViewSet

router = DefaultRouter()
router.register(
    r"user-detail",
    UserDetailViewSet,
    basename="user-detail",
)

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "cab/",
        include((router.urls, "cab"), namespace="cab"),
    ),
]
