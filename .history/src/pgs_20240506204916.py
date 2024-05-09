import gnupg
from stegano import lsb
import os

def read_pgp_key(file_path):
    hidden_data = lsb.reveal("image.jpeg")
    # Specify the path to the gpg binary
    gpg_binary = '/opt/homebrew/bin/gpg'

    # Initialize a GPG object
    gpg = gnupg.GPG(binary=gpg_binary)

    

    # Read the PGP key file
    with open(file_abs_path, 'r') as key_file:
        key_data = key_file.read()

    # Import the key
    imported_keys = gpg.import_keys(key_data)
    print(imported_keys, "here")
    # Get the imported key
    keys = gpg.list_keys(True)
    if keys:
        return keys[0]
    else:
        return None