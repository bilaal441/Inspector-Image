from PIL import Image

# Function to extract hidden PGP key from an image
def extract_pgp_key(image_path):
    # Open the image
    img = Image.open(image_path)
    # Get data from the image
    key_data = img.getdata()
    # Flatten the key data
    key_data_flat = [x for sublist in key_data for x in sublist]
    # Convert data to string
    key_str = ''.join([chr(i) for i in key_data_flat])
    # Split the string into chunks of 2 characters (hexadecimal representation)
    hex_chunks = [key_str[i:i+2] for i in range(0, len(key_str), 2)]
    # Filter out non-hexadecimal characters
    hex_filtered = [chunk for chunk in hex_chunks if all(c in '0123456789ABCDEFabcdef' for c in chunk)]
    # Combine the filtered hexadecimal chunks into a string
    key_hex = ''.join(hex_filtered)
    # Convert hexadecimal string to bytes
    key_bytes = bytes.fromhex(key_hex)
    # Convert bytes to string
    key_str = key_bytes.decode('utf-8')
    # Construct the PGP public key block
    pgp_key_block = "-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
    pgp_key_block += "Version: 01\n\n"
    pgp_key_block += key_str + "\n"
    pgp_key_block += "-----END PGP PUBLIC KEY BLOCK-----\n"
    # Output the PGP public key block
    print(pgp_key_block)
    return pgp_key_block


