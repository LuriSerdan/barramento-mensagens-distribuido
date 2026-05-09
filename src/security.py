from cryptography.fernet import Fernet # type: ignore

class CryptoLayer:
    def __init__(self, key=None):
        # Em um sistema real, a chave seria distribuída via troca assimétrica
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message: str) -> str:
        return self.cipher.encrypt(message.encode()).decode()

    def decrypt(self, encrypted_message: str) -> str:
        return self.cipher.decrypt(encrypted_message.encode()).decode()