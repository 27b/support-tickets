from django.urls import path

from .views import AccountLoginView


urlpatterns = [
    path('signin', AccountLoginView.as_view(), name='api_account_signin')
]