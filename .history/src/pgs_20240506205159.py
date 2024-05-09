import gnupg
from stegano import lsb
import os

def read_pgp_key(file_path):
    # Get the absolute path of the file
    file_abs_path = os.path.abspath(file_path)
    hidden_data = lsb.reveal(file_abs_path)
    # Specify the path to the gpg binary
    gpg_binary = '/opt/homebrew/bin/gpg'

    # Initialize a GPG object
    gpg = gnupg.GPG(binary=gpg_binary)

  # Import the key
    import_result = gpg.import_keys(hidden_data)
    return  import_result