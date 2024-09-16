from io import BytesIO
import base64

#Converts an image into a data URI in Base64 format
def convert_image_to_data_uri(image):
    data = BytesIO()
    image.save(data, format="PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return f"data:image/png;base64,{encoded_img_data.decode('utf-8')}"