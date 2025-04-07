# secure_openssl.py

import os
import re
import sys
import logging
import getpass
import tempfile
import argparse
import subprocess

def setup_logging():
    logging.basicConfig(filename="secure_openssl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_openssl(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"OpenSSL command failed: {e.stderr}")
        return None

def validate_path(file_path):
    return re.match(r'^[a-zA-Z0-9_/.-]+$', file_path) is not None

def encrypt_file(input_file, encrypted_file, password):
    command = ["openssl", "enc", "-aes-256-cbc", "-salt", "-in", input_file, "-out", encrypted_file, "-pass", f"pass:{password}"]
    return run_openssl(command)

def decrypt_file(encrypted_file, decrypted_file, password):
    command = ["openssl", "enc", "-aes-256-cbc", "-d", "-in", encrypted_file, "-out", decrypted_file, "-pass", f"pass:{password}"]
    return run_openssl(command)

def hash_file(file_path):
    command = ["openssl", "dgst", "-sha256", file_path]
    return run_openssl(command)

setup_logging()
parser = argparse.ArgumentParser(description="Secure OpenSSL File Operations")
parser.add_argument("mode", choices=["encrypt", "decrypt", "hash"], help="Operation mode")
parser.add_argument("file", help="Input file path")
parser.add_argument("--password", help="Encryption password", required=False)
args = parser.parse_args()
if not validate_path(args.file):
    logging.error("Invalid file path format.")
    sys.exit(1)
password = args.password if args.password else getpass.getpass("Enter password: ")
if args.mode == "encrypt":
    encrypt_file(args.file, f"{args.file}.enc", password)
elif args.mode == "decrypt":
    decrypt_file(args.file, f"{args.file}.dec", password)
elif args.mode == "hash":
    print(hash_file(args.file))