from PIL import Image

# Function to extract hidden PGP key from an image
def extract_pgp_key(image_path):
    # Open the image
    img = Image.open(image_path)
    # Get data from the image
    key_data = img.getdata()
    # Convert data to string
    key_str = ''.join([chr(i) for i in key_data])
    # Decode hexadecimal string to bytes
    key_bytes = bytes.fromhex(key_str)
    # Convert bytes to string
    key_str = key_bytes.decode('utf-8')
    # Convert string to hexadecimal
    key_hex = bytearray.fromhex(key_str)
    # Write hexadecimal data to a file
    with open("extracted_public_key.asc", "wb") as f:
        f.write(key_hex)

# Example usage
extract_pgp_key("image_with_hidden_key.png")

