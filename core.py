import os
import time
import hmac
from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from argon2.low_level import hash_secret_raw, Type

class PetoronTimeBurnCipher:
    SIGNATURE = b'PTBC'
    SALT_SIZE = 16
    KEY_SIZE = 32
    HMAC_SIZE = 64

    def __init__(self, password: str):
        self.password = password.encode()

    def _derive_keys(self, salt: bytes) -> tuple:
        key_material = hash_secret_raw(
            secret=self.password,
            salt=salt,
            time_cost=3,
            memory_cost=2**18,
            parallelism=4,
            hash_len=self.KEY_SIZE * 2,
            type=Type.ID
        )
        return key_material[:self.KEY_SIZE], key_material[self.KEY_SIZE:]

    def encrypt(self, plaintext: bytes, ttl_seconds: int) -> bytes:
        expiry_time = int(time.time()) + ttl_seconds
        salt = os.urandom(self.SALT_SIZE)
        enc_key, hmac_key = self._derive_keys(salt)
        iv = os.urandom(16)
        cipher = AES.new(enc_key, AES.MODE_CFB, iv)
        ciphertext = cipher.encrypt(plaintext)

        body = self.SIGNATURE + expiry_time.to_bytes(8, 'big') + salt + iv + ciphertext
        tag = hmac.new(hmac_key, body, SHA512).digest()
        return body + tag

    def decrypt(self, encrypted_data: bytes) -> bytes:
        if not encrypted_data.startswith(self.SIGNATURE):
            raise ValueError("Invalid signature")
        if len(encrypted_data) < 44 + self.HMAC_SIZE:
            raise ValueError("Corrupted or incomplete data")

        body = encrypted_data[:-self.HMAC_SIZE]
        received_hmac = encrypted_data[-self.HMAC_SIZE:]

        expiry_time = int.from_bytes(encrypted_data[4:12], 'big')
        if time.time() > expiry_time:
            raise ValueError("Expired")

        salt = encrypted_data[12:28]
        iv = encrypted_data[28:44]
        ciphertext = encrypted_data[44:-self.HMAC_SIZE]

        enc_key, hmac_key = self._derive_keys(salt)
        calc_hmac = hmac.new(hmac_key, body, SHA512).digest()

        if not hmac.compare_digest(calc_hmac, received_hmac):
            raise ValueError("HMAC verification failed")

        cipher = AES.new(enc_key, AES.MODE_CFB, iv)
        return cipher.decrypt(ciphertext)

    def destroy(self):
        self.password = b''



