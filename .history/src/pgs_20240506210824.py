import gnupg
from stegano import lsb
import os

def read_pgp_key(file_path):
    # Get the absolute path of the file
    file_abs_path = os.path.abspath(file_path)

    try:
        # Try to reveal the hidden data
        hidden_data = lsb.reveal(file_abs_path)
        
        # Decode the hidden data
        hidden_data = hidden_data.decode('utf-8')
    except IndexError:
        # If an IndexError is raised, return an error message
        return "Error: The hidden data extends beyond the boundaries of the image."

    # Specify the path to the gpg binary
    gpg_binary = '/opt/homebrew/bin/gpg'

    # Initialize a GPG object
    gpg = gnupg.GPG(binary=gpg_binary)

    # Import the key
    import_result = gpg.import_keys(hidden_data)
    
    if import_result.count == 0:
        return "Error: No valid keys found in the hidden data."
    else:
        return "Key(s) imported successfully."

# Example usage:
pgp_key_file = 'hidden_key_image.png'
result = read_pgp_key(pgp_key_file)
print(result)
