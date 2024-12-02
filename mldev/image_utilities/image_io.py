import base64
import mimetypes
import numpy as np
from PIL import Image
from io import BytesIO
import requests

def get_mime_type(file_path):
    """
    Get the MIME type of the image file.

    Args:
        file_path (str): Path to the image file.

    Returns:
        str: MIME type of the image.
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

def array_to_mime_type(img_array):
    """
    Get the MIME type from an image array by attempting to save it as a JPEG or PNG.

    Args:
        img_array (numpy.ndarray): Image represented as a NumPy array.

    Returns:
        str: Inferred MIME type of the image.
    """
    img = Image.fromarray(img_array)
    with BytesIO() as buffer:
        try:
            img.save(buffer, format="JPEG")
            return "image/jpeg"
        except Exception:
            buffer.truncate(0)
            buffer.seek(0)
            img.save(buffer, format="PNG")
            return "image/png"

def image_to_base64(file_path):
    """
    Convert an image to Base64 data.

    Args:
        file_path (str): Path to the image file.

    Returns:
        str: Base64-encoded string of the image.
    """
    mime_type, = get_mime_type(file_path)
    
    if not mime_type:
        raise ValueError("Cannot determine the MIME type of the file")
    
    # Read the file in binary mode
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    
    # Encode the binary data to Base64
    base64_data = base64.b64encode(binary_data).decode('utf-8')
    
    # Combine MIME type and Base64 string
    base64_with_mime = f"data:{mime_type};base64,{base64_data}"
    return base64_with_mime

def image_to_bytes(file_path):
    """
    Convert an image to bytes.

    Args:
        file_path (str): Path to the image file.

    Returns:
        bytes: Byte data of the image.
    """
    with open(file_path, "rb") as img_file:
        byte_data = img_file.read()
    return byte_data

def image_to_array(file_path):
    """
    Convert an image to a NumPy array.

    Args:
        file_path (str): Path to the image file.

    Returns:
        numpy.ndarray: Image represented as a NumPy array.
    """
    with Image.open(file_path) as img:
        img_array = np.array(img)
    return img_array

def array_to_base64(img_array, mime_type="image/jpeg"):
    """
    Convert a NumPy image array to Base64 data.

    Args:
        img_array (numpy.ndarray): Image represented as a NumPy array.
        mime_type (str): MIME type of the image (default: "image/jpeg").

    Returns:
        str: Base64-encoded string of the image.
    """
    img = Image.fromarray(img_array)
    with BytesIO() as buffer:
        img.save(buffer, format=mime_type.split("/")[1].upper())
        base64_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return base64_data

def array_to_bytes(img_array, mime_type="image/jpeg"):
    """
    Convert a NumPy image array to bytes.

    Args:
        img_array (numpy.ndarray): Image represented as a NumPy array.
        mime_type (str): MIME type of the image (default: "image/jpeg").

    Returns:
        bytes: Byte data of the image.
    """
    img = Image.fromarray(img_array)
    with BytesIO() as buffer:
        img.save(buffer, format=mime_type.split("/")[1].upper())
        byte_data = buffer.getvalue()
    return byte_data


def image_url_to_array(image_url):
    """
    Convert an image URL to a NumPy array.

    Args:
        image_url (str): URL of the image.

    Returns:
        numpy.ndarray: Image represented as a NumPy array.
    """
    response = requests.get(image_url)
    response.raise_for_status()
    with Image.open(BytesIO(response.content)) as img:
        img_array = np.array(img)
    return img_array

def base64_to_array(base64_data):
    """
    Convert Base64 to a NumPy image array.

    """
    header, base64_data = base64_data.split(",")
    inferred_mime = header.split(":")[1].split(";")[0]
    byte_data = base64.b64decode(base64_data)
    img = Image.open(BytesIO(byte_data))
    img_array = np.array(img)
    return inferred_mime,img_array

def bytes_to_array(input_data:bytes) :
    img = Image.open(BytesIO(input_data))
    img_array = np.array(img)
    return img_array

def convert_to_array(input_data, mime_type=None):
    """
    Convert input data (URL, Base64, bytes) to a NumPy image array.

    Args:
        input_data: The input image data, which can be a URL, Base64 string, or bytes.
        mime_type (str, optional): MIME type of the input data. Defaults to None.

    Returns:
        tuple: A tuple containing (numpy.ndarray, str) where the first element is the image array and the second is the MIME type.
    """
    if isinstance(input_data, str):
        if input_data.startswith("http://") or input_data.startswith("https://"):
            img_array = image_url_to_array(input_data)
            inferred_mime = "image/jpeg"  # Default assumption for URL images
        elif len(input_data) % 4 == 0 and "/" in input_data and ";base64," in input_data:
            inferred_mime,img_array = base64_to_array(base64_data)
        else:
            raise ValueError("Invalid string format. Provide a valid URL or Base64 string.")
    elif isinstance(input_data, bytes):
        img_array = bytes_to_array(input_data)
        inferred_mime = mime_type if mime_type else "image/jpeg"
    else:
        raise TypeError("Unsupported input type. Provide a URL, Base64 string, or bytes.")
    return img_array, inferred_mime

# Example usage
if __name__ == "__main__":
    file_path = "path_to_your_image.jpg"  # Replace with your image file path

    mime_type = get_mime_type(file_path)
    print(f"MIME type: {mime_type}")

    base64_data = image_to_base64(file_path)
    print(f"Base64 data: {base64_data[:100]}... (truncated)")

    byte_data = image_to_bytes(file_path)
    print(f"Bytes data: {byte_data[:100]}... (truncated)")

    img_array = image_to_array(file_path)
    print(f"Image array shape: {img_array.shape}")

    # Converting array back to base64 and bytes
    array_base64 = array_to_base64(img_array, mime_type)
    print(f"Array to Base64: {array_base64[:100]}... (truncated)")

    array_bytes = array_to_bytes(img_array, mime_type)
    print(f"Array to Bytes: {array_bytes[:100]}... (truncated)")

    # Inferring MIME type from array
    inferred_mime_type = array_to_mime_type(img_array)
    print(f"Inferred MIME type from array: {inferred_mime_type}")

    # Convert image URL to array
    image_url = "https://example.com/path_to_your_image.jpg"  # Replace with a valid image URL
    img_array_from_url = image_url_to_array(image_url)
    print(f"Image array from URL shape: {img_array_from_url.shape}")

    # Convert image array from URL to base64 and bytes
    url_array_base64 = array_to_base64(img_array_from_url)
    print(f"URL Array to Base64: {url_array_base64[:100]}... (truncated)")

    url_array_bytes = array_to_bytes(img_array_from_url)
    print(f"URL Array to Bytes: {url_array_bytes[:100]}... (truncated)")

    # Convert mixed input to array
    mixed_input = base64_data  # Replace with Base64, URL, or bytes input
    mixed_array, mixed_mime = convert_to_array(mixed_input)
    print(f"Mixed input array shape: {mixed_array.shape}, MIME type: {mixed_mime}")
