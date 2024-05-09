from PIL import Image

# Function to extract hidden PGP key from an image
def extract_pgp_key(image_path):
    # Open the image
    img = Image.open(image_path)
    # Get data from the image
    key_data = img.getdata()
    # Flatten the key data
    key_data_flat = [x for sublist in key_data for x in sublist]
    # Convert data to hexadecimal string
    key_str = ''.join([f"{i:02X}" for i in key_data_flat if isinstance(i, int)])
    # Insert newline characters for formatting
    key_str = '\n'.join([key_str[i:i+64] for i in range(0, len(key_str), 64)])
    # Construct the PGP public key block
    pgp_key_block = "-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
    pgp_key_block += "Version: 01\n\n"
    pgp_key_block += key_str + "\n"
    pgp_key_block += "-----END PGP PUBLIC KEY BLOCK-----\n"
    return pgp_key_block

# Example usage
extracted_key = extract_pgp_key("image_with_hidden_key.png")
print(extracted_key)
