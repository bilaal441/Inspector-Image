import re

def extract_pgp_key(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
           
           
    # Search for PGP public key pattern
    pattern = r'-----BEGIN PGP PUBLIC KEY BLOCK-----(.*?)-----END PGP PUBLIC KEY BLOCK-----'
    pgp_public_key = re.search(pattern, image_data.decode('latin-1'), re.DOTALL)

    if pgp_public_key:
        return pgp_public_key.group(0)
    else:
        return None
