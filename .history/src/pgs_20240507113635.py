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
    # Decode hexadecimal string to bytes
    key_bytes = bytes.fromhex(key_str)
    # Write bytes to a file
    with open("extracted_public_key.asc", "wb") as f:
        f.write(key_bytes)

