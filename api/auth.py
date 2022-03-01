from rest_framework.authtoken.views import ObtainAuthToken
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



'''
# Use this in url for token
#from django.urls import path
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