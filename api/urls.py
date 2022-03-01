from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
# router.register('signup/', views.SignUP.as_view, basename='userAccount'),

urlpatterns  = [
   path('', include(router.urls)),
   # path('signup/', views.sign_up),
   path('signup/', views.SignUP.as_view(), name="signup"),
   # path('gettoken/', obtain_auth_token)
]