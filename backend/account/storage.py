from uuid import uuid4

from django.contrib.auth.models import User


TOKENS_IN_MEMORY = {}

class TokenStorageMemory: 

    @staticmethod
    def create_token() -> str:
        token = ''
        while token == '':
            new_token = uuid4().hex + uuid4().hex
            if not TOKENS_IN_MEMORY.get(new_token):  # check token not repeated
                token = new_token
        return token

    @staticmethod
    def save_token(user: User, token: str) -> None:
        TOKENS_IN_MEMORY[token] = user
    
    @staticmethod
    def get_account(token: str) -> User:
        return TOKENS_IN_MEMORY.get(token)