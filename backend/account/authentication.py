from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .storage import TokenStorageMemory


class CustomTokenAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return None

        try:
            user = TokenStorageMemory.get_account(token)

            if not user:
                return None

        except Exception as error:
            raise AuthenticationFailed('No such user')

        return (user, None)