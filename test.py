# Run it with:
# python test.py demo_input.jpg

import sys
import requests
import base64
from io import BytesIO
from PIL import Image

#Read filename to send as base64 encoding
img_name = sys.argv[1:][0]
with open(img_name, "rb") as f:
    bytes = f.read()
    encoded = base64.b64encode(bytes).decode('utf-8')

model_inputs = {'img_bytes': encoded }
res = requests.post('http://localhost:8000/', json = model_inputs)

image_byte_string = res.json()["image_base64"]
image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")