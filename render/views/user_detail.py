from rest_framework.viewsets import ModelViewSet


from render.models import UserDetail
from render.seriallizer.user_detail import UserDetailSerializer


class UserDetailViewSet(ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
