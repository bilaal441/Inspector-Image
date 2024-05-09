import gnupg
import os

def read_pgp_key(file_path):
   
# binary
    gpg_binary = '/opt/homebrew/bin/gpg'
    # Initialize a GPG object
    gpg = gnupg.GPG(binary=gpg_binary)

    # Get the absolute path of the file
    file_abs_path = os.path.abspath(file_path)
     print(file_abs_path)
    # Read the PGP key file
    with open(file_abs_path, 'r') as key_file:
        key_data = key_file.read()

    # Import the key
    imported_keys = gpg.import_keys(key_data)

    # Get the imported key
    key = gpg.list_keys(True)[0]

    return key
# # Example usage
# key_file_path = 'path/to/pgp_key.asc'
# pgp_key = read_pgp_key(key_file_path)

# # Display the PGP key details
# print("PGP Key Details:")
# print("Key ID:", pgp_key['keyid'])
# print("User ID:", pgp_key['uids'])
# print("Fingerprint:", pgp_key['fingerprint'])
# print("Key Length:", pgp_key['key_length'])
