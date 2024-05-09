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
        return f"Lat/Lon:\t({latitude:.4f}) / ({longitude:.4f})"
  
  return None

