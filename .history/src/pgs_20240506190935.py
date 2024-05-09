import gnupg
import os

def read_pgp_key(file_path):
    # Specify the path to the gpg binary
    gpg_binary = '/opt/homebrew/bin/gpg'

    # Initialize a GPG object
    gpg = gnupg.GPG(binary=gpg_binary)

    # Get the absolute path of the file
    file_abs_path = os.path.abspath(file_path)

    # Read the PGP key file
    with open(file_abs_path, 'r') as key_file:
        key_data = key_file.read()

    # Import the key
    imported_keys = gpg.import_keys(key_data)
    
    # Get the imported key
    keys = gpg.list_keys(True)
    if keys:
        return keys[0]
    else:
        return None