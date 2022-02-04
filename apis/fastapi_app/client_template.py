import requests
import json
import cv2

def upload_image_as_bytearray(image_array):
    api_end_point = "http://0.0.0.0:8888/upload/image"
    content_type = "image/jpeg"
    headers = {"content-type":content_type}
    _,image_encoded = cv2.imencode(".jpg",image_array)

    try:
        response = requests.post(api_end_point,image_encoded.tobytes(),headers=headers)
        print(response)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(e.response.text)

if __name__=="__main__":
    image_path = "/home/ubuntu/Downloads/postman.jpg"
    image_url = ""
    image_array = cv2.imread(image_path)
    response = upload_image_as_bytearray(image_array)