# File Encrypter/Decrypter 🔐

A simple Python tool to encrypt and decrypt files using AES-128 symmetric encryption via the Fernet scheme.

## Features
- 🔑 Auto-generate a secure `secret.key` (AES-128).
- 🔒 Encrypt any file (text, images, etc.) to `.encrypted`.
- 🔓 Decrypt `.encrypted` files back to their original form.


## Installation
1. Install the `cryptography` library:
   ```bash
   pip install cryptography