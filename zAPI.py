######################################################################################################################################
#######################################          Token Authentication API            #######################################
######################################################################################################################################

'''
# If token needs to be Generated Automatically on user creation.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''
'''
# Creating token
    pip install httpie
    http POST http://127.0.0.1:5100/account/gettoken/ username="admin" password="1234"
'''

'''from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Custome class For Token
class CustomAuhToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id':user.pk,
            'email': user.email
        })

# Use this in url for token

from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuhToken



# Creating token
# pip install httpie
# http POST http://127.0.0.1:5100/account/gettoken/ username="admin" password="1234"

urlpatterns  = [
   path('gettoken/', CustomAuhToken.as_view())
#    path('gettoken/', obtain_auth_token)
]

'''

'''
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import User
from .serializers import UserSerializer

# Create your views here.

from rest_framework.permissions import BasePermission
from rest_framework.authentication import SessionAuthentication

class myPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [myPermission]
'''

######################################################################################################################################
#######################################          Authentication And Permissions API            #######################################
######################################################################################################################################


''' Learn custom Authontication if Need it '''

################################## API Using ModelViewSet Custom permissions #########################################################
'''
from rest_framework.permissions import BasePermission
from rest_framework.authentication import SessionAuthentication

class myPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [myPermission]
'''


################################## API Using ModelViewSet IsAuthenticated IsAdminUser AllowAny IsAuthenticatedOrReadOnly DjangoModelPermissions ##################################
'''
When working with AJAX style API with SessionAuthonetication, need to make sure valid csrf tocken for "unsafe" HTTP methods calls such as PUT, PATCH, POST, AND DELETE 
("safe" methods are GET, HEAD AND OPTION)
'''
'''
# set urlpatterns path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

'''

################################## API Using ModelViewSet IsAuthenticated IsAdminUser AllowAny ##################################
'''
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
'''

################################## API Using ReadOnlyModelViewSet ModelViewSet ##################################
'''
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''

################################## API Using ViewSets ViewSet ##################################
'''
from rest_framework import viewsets, status
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    def list(self, request):

        print('********** GET ************')
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detal: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'create req'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'update req'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial req'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        stu = User.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'Delete req'})
'''

################################## API Using concrete generic ListCreateAPIView RetrieveUpdateDestroyAPIView etc ##################################
'''
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LCUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RUDUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''

################################## API Using concrete generic ListAPIView CreateAPIView RetrieveAPIView UpdateAPIView DestroyAPIView ##################################
'''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

class LCUser(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RUDUser(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''

################################## API Using GenericAPIView + Mixin ##################################
'''
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin 

# List and Create - PK Not required 
class LCUser(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrive, Update and Delete - PK required 
class RUDUser(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

################################## API Using  APIView ##################################
'''
# Class based 

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = User.objects.get(id=pk)
            serializer = UserSerializer(stu)
            return Response({'msg': 'get req', "data":serializer.data})
        stu = User.objects.all()
        serializer = UserSerializer(stu, many=True)
        return Response({'msg': 'Get req', "data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post req'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            stu = User.objects.get(id=pk)
            stu.delete()
            return Response({'msg': 'Delete req'})
'''

################################## API Using APapi_view ##################################
'''
# If Authentication needs to be used in Fuction use Decorators
# Function based 

from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @authentication_classes = ([BasicAuthentication])
# @permission_classes = ([IsAuthenticated])
def UserViewSet(request, pk = None):
    if request.method == 'GET':
        if pk is not None:
            stu = User.objects.get(id=pk)
            serializer = UserSerializer(stu)
            return Response({'msg': 'get req', "data":serializer.data})
        stu = User.objects.all()
        serializer = UserSerializer(stu, many=True)
        return Response({'msg': 'get req', "data":serializer.data})
'''



# from django.core.management.base import BaseCommand, CommandError
# from django.contrib.auth.models import User
    # def handle(self, *args, **options):
    #     # The magic line
    #     User.objects.create_user(username= 'rmx',
    #                             email='superuser@super.com',
    #                             password='rmx55',
    #                             is_staff=True,
    #                             is_active=True,
    #                             is_superuser=True
    #     )
