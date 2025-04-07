import subprocess
import os
import sys
import tempfile
import logging
from getpass import getpass

import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Secure OpenSSL Wrapper")
parser.add_argument("--password", type=str, help="Encryption password")
parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, help="Choose operation mode")
args = parser.parse_args()

import re

# Configure logging
logging.basicConfig(filename="secure_openssl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def is_valid_path(path):
    # Basic regex to prevent dangerous characters and validate format
    return bool(re.match(r'^[\w\-.\\/]+$', path)) and os.path.abspath(path) == path

def run_openssl(command):
    """Executes an OpenSSL command securely."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"OpenSSL command failed: {e.stderr}")
    return None

def generate_private_key(key_path):
    """Generates a secure RSA private key."""
    command = ["openssl", "genpkey", "-algorithm", "RSA", "-out", key_path, "-aes256"]
    return run_openssl(command)

def generate_public_key(private_key, public_key):
    """Generates a public key from a private key."""
    command = ["openssl", "rsa", "-in", private_key, "-pubout", "-out", public_key]
    return run_openssl(command)

def create_self_signed_certificate(private_key, cert_path, days=365):
    """Creates a self-signed certificate."""
    command = ["openssl", "req", "-x509", "-new", "-key", private_key, "-out", cert_path, "-days", str(days), "-subj", "/CN=SecureApp"]
    return run_openssl(command)

def encrypt_file(input_file, encrypted_file, password):
    """Encrypts a file securely using AES-256."""
    command = ["openssl", "enc", "-aes-256-cbc", "-salt", "-in", input_file, "-out", encrypted_file, "-pass", f"pass:{password}"]
    return run_openssl(command)

def decrypt_file(encrypted_file, decrypted_file, password):
    """Decrypts a file securely."""
    command = ["openssl", "enc", "-aes-256-cbc", "-d", "-in", encrypted_file, "-out", decrypted_file, "-pass", f"pass:{password}"]
    return run_openssl(command)

def hash_file(file_path):
    """Computes SHA-256 hash of a file."""
    command = ["openssl", "dgst", "-sha256", file_path]
    return run_openssl(command)

if __name__ == "__main__":
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            private_key = os.path.abspath(os.path.join(tmpdir, "private_key.pem"))
            public_key = os.path.abspath(os.path.join(tmpdir, "public_key.pem"))
            cert_path = os.path.abspath(os.path.join(tmpdir, "certificate.crt"))
            plaintext_file = os.path.abspath(os.path.join(tmpdir, "plaintext.txt"))
            encrypted_file = os.path.abspath(os.path.join(tmpdir, "encrypted.txt"))
            decrypted_file = os.path.abspath(os.path.join(tmpdir, "decrypted.txt"))

            # Validate paths before proceeding
            for path in [private_key, public_key, cert_path, plaintext_file, encrypted_file, decrypted_file]:
                if not is_valid_path(path):
                    raise ValueError(f"Invalid path: {path}")

            # Create dummy plaintext file for encryption
            with open(plaintext_file, "w") as f:
                f.write("This is a secure test file.")

            # Generate keys and certificate
            generate_private_key(private_key)
            generate_public_key(private_key, public_key)
            create_self_signed_certificate(private_key, cert_path)

            # Encrypt and Decrypt
            
            password = args.password if args.password else getpass("Enter encryption password: ")

            if args.mode == "encrypt":
                encrypt_file(plaintext_file, encrypted_file, password)
                print("File encrypted successfully.")
                hash_result = hash_file(plaintext_file)
                print(f"SHA-256 hash of plaintext file: {hash_result.strip()}")
            elif args.mode == "decrypt":
                decrypt_file(encrypted_file, decrypted_file, password)
                print("File decrypted successfully.")
                hash_result = hash_file(decrypted_file)
                print(f"SHA-256 hash of decrypted file: {hash_result.strip()}")
            else:
                print("Invalid mode selected.")
                sys.exit(1)
:
    """Decrypts a file securely."""
    command = ["openssl", "enc", "-aes-256-cbc", "-d", "-in", encrypted_file, "-out", decrypted_file, "-pass", f"pass:{password}"]
    return run_openssl(command)

def hash_file(file_path):
    """Computes SHA-256 hash of a file."""
    command = ["openssl", "dgst", "-sha256", file_path]
    return run_openssl(command)

if __name__ == "__main__":
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            private_key = os.path.abspath(os.path.join(tmpdir, "private_key.pem"))
            public_key = os.path.abspath(os.path.join(tmpdir, "public_key.pem"))
            cert_path = os.path.abspath(os.path.join(tmpdir, "certificate.crt"))
            plaintext_file = os.path.abspath(os.path.join(tmpdir, "plaintext.txt"))
            encrypted_file = os.path.abspath(os.path.join(tmpdir, "encrypted.txt"))
            decrypted_file = os.path.abspath(os.path.join(tmpdir, "decrypted.txt"))

            # Validate paths before proceeding
            for path in [private_key, public_key, cert_path, plaintext_file, encrypted_file, decrypted_file]:
                if not is_valid_path(path):
                    raise ValueError(f"Invalid path: {path}")

            # Create dummy plaintext file for encryption
            with open(plaintext_file, "w") as f:
                f.write("This is a secure test file.")

            # Generate keys and certificate
            generate_private_key(private_key)
            generate_public_key(private_key, public_key)
            create_self_signed_certificate(private_key, cert_path)

            # Encrypt and Decrypt
            password = getpass("Enter encryption password: ")
            encrypt_file(plaintext_file, encrypted_file, password)
            decrypt_file(encrypted_file, decrypted_file, password)

            # Hash the decrypted file
            hash_result = hash_file(decrypted_file)
            logging.info(f"SHA-256 Hash: {hash_result.strip()}")

            print("Secure OpenSSL operations completed successfully.")

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        sys.exit(1)
