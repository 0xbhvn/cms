from django.urls import path

from accounts.views import AccountList, AccountRegister, AccountDetail, BlacklistToken, CurrentUser

app_name = 'accounts'

urlpatterns = [
    path('current_user/', CurrentUser.as_view()),
    path('', AccountList.as_view()),
    path('register/', AccountRegister.as_view()),
    path('<username>/', AccountDetail.as_view()),
    path('logout/blacklist/', BlacklistToken.as_view(), name='logout')
]
