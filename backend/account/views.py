from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response

from account.authentication import TokenStorageMemory


class AccountLoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        # Check user credentials
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({'error': 'Invalid credentials'}, status=401)
        
        token = TokenStorageMemory.create_token()
 
        # Store user token releated with User object in a key-value store
        TokenStorageMemory.save_token(user, token)

        return Response({ 'token': token })

