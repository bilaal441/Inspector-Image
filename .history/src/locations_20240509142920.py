from PIL import Image
from PIL.ExifTags import TAGS

def get_image_coordinates(image_path):
  image = Image.open(image_path)
  exif_data = image._getexif()

  if exif_data is not None:
    for tag, value in exif_data.items():
      if TAGS.get(tag) == 'GPSInfo':
        latitude = value[2][0] + value[2][1] / 60 + value[2][2] / 3600
        longitude = value[4][0] + value[4][1] / 60 + value[4][2] / 3600

        # Convert latitude and longitude to directions
        latitude_direction = 'N' if value[1] == 'N' else 'S'
        longitude_direction = 'E' if value[3] == 'E' else 'W'

        return f"Location: {latitude:.4f}°{latitude_direction}, {longitude:.4f}°{longitude_direction}"

  return None

