from django.urls import path, include
from .views import AccountLoginView, AccountSingUpView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='account-login'),
    path('accounts/signup', AccountSingUpView.as_view(), name='account-signup'),
]
