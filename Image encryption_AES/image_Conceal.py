#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import numpy as np
import hashlib
import os

def generate_aes_key_from_phone(phone_number):
    hash_object = hashlib.sha256(phone_number.encode())
    return hash_object.digest()[:16]  # 128-bit key


def encrypt_image(image_path, aes_key, rsa_public_key):
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # AES暗号化
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv
    ciphertext = cipher_aes.encrypt(pad(image_bytes, AES.block_size))

    # AES鍵のRSA暗号化
    rsa_cipher = PKCS1_OAEP.new(RSA.import_key(rsa_public_key))
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    return iv, ciphertext, encrypted_aes_key

# ユーザーのホームディレクトリを取得
home_directory = os.path.expanduser("~")

# model.h5のパスを指定
image_path = os.path.join(home_directory, "Downloads", "sample.png")

phone_number = "1234567890"  # 例: ユーザーの電話番号
aes_key = generate_aes_key_from_phone(phone_number)

# RSA鍵ペアの生成
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 公開鍵と秘密鍵をファイルに保存
with open("private.pem", "wb") as f:
    f.write(private_key)

with open("public.pem", "wb") as f:
    f.write(public_key)

iv, ciphertext, encrypted_aes_key = encrypt_image(image_path, aes_key, public_key)