from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/login/', views.LoginView.as_view(), name='auth-login'),
    path('user/signup/', views.RegisterUserView.as_view(), name='auth-signup'),
]
