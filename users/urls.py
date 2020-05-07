from django.urls import path
from users.views import UserView, UserDetail, UserExist, LoginView
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    path('', UserView.as_view(), name='user_list'),
    path('<str:username>/', UserDetail.as_view(), name='user_detail'),
    path('check-existing-user/<str:username>/',
         UserExist.as_view(), name='user_exist'),
    path('auth/login/', LoginView.as_view(), name='user_login'),
    path('api-token-auth/', obtain_jwt_token, name='user_token'),
    path('api-token-refresh/', refresh_jwt_token, name='token_refresh'),
    path('api-token-verify/', verify_jwt_token, name='token_verify'),
]