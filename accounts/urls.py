from django.urls import path

from accounts.views import AccountList, AccountRegister, AccountDetail

app_name = 'accounts'

urlpatterns = [
    path('', AccountList.as_view()),
    path('register/', AccountRegister.as_view()),
    path('<username>/', AccountDetail.as_view()),
]
