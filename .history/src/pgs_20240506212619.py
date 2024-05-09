from PIL import Image
from stegano import lsb
import base64
import os

def extract_pgp_key(image_path):
    file_abs_path = os.path.abspath(file_path)
    # Read the image
    image = Image.open(image_path)
    print("Image loaded successfully:", image)

    # Extract hidden data
    try:
        secret_data = lsb.reveal(image)
        print("Hidden data found in the image:", secret_data)
    except IndexError:
        return "Error: No hidden data found in the image."

    # Continue with the rest of your code...
