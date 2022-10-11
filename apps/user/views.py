from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.permissions import IsAdmin, IsEditorial, IsAuthor

from apps.user.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            permission_classes = (IsAuthenticated, IsAdmin)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated, IsAdmin | IsEditorial |
                                  IsAuthor)
        else:
            permission_classes = (IsAuthenticated, )
        return [permission() for permission in permission_classes]


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={
            'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user_id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'type': user.type
            }
        )


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        Token.objects.filter(user=user).delete()

        return Response({'message': 'Exito'})
