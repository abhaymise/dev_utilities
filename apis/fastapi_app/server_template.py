from fastapi import FastAPI,Request
import numpy as np
import cv2
from pathlib import Path
import uvicorn

app = FastAPI()
app_name = "sample fast api server"

def time_function(func):
    pass

@app.get("/")
def whoami():
    return f" hi am {app_name}"

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/upload/image")
async def upload_image(request : Request):
    upload_dir = "static"
    Path(upload_dir).mkdir(exist_ok=True,parents=True)
    image_name = "test"
    ext = ".jpeg"
    image_path = f"{upload_dir}/{image_name}{ext}"
    # image_array = read_image_from_request(request)
    whole_byte_array = b''
    async for byte_block in request.stream():
        whole_byte_array += byte_block
    image_array = np.fromstring(whole_byte_array, np.uint8)
    image_array = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    print(f"image saved at {image_path}")
    cv2.imwrite(image_path,image_array)
    return {"message":"sucess","image_path":image_path}

def start_server():
    uvicorn.run(app,port=8888,host="0.0.0.0")#,reload=True, debug=True)

if __name__=="__main__":
    # to run in debug mode
    # uvicorn server_template:app --reload --port 8888
    start_server()


