import cv2
import numpy as np
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app_name = "sample fast api server"

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",#origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from functools import wraps
import time
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@app.get("/")
def whoami():
    return f" hi am {app_name}"

@app.get("/health")
def health():
    return {"status":"ok"}

@timeit
def deserialize_to_image_array(image_byte_array ):
    image_np_array = np.frombuffer(image_byte_array,np.uint8)
    image_array = cv2.imdecode(image_np_array,cv2.IMREAD_COLOR)
    return image_array

@timeit
def save_image_array(image_array,file_name,ext):
    saving_dir = "static"
    image_path = f"{saving_dir}/{file_name}{ext}"
    cv2.imwrite(image_path,image_array)
    return "success"

@timeit
@app.post("/upload/image/")
async def upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        file_content = await file.read()
        file_name = file.filename
        file_content_type = file.content_type
        if file_content_type == "image/jpeg":
            image_array = deserialize_to_image_array(file_content)
            save_image_array(image_array,file_name=file_name,ext="jpeg")
        return {"filename": file_name,"size":image_array.shape}

@timeit
@app.post("/upload/images/")
async def create_upload_files(files: list[UploadFile]):
    file_count = len(files)
    filenames = [file.filename for file in files]
    file_upload_path = []
    file_size = []
    for file in files:
        file_content = await file.read()
        file_name = file.filename
        file_content_type = file.content_type
        if file_content_type == "image/jpeg":
            image_array = np.fromstring(file_content,np.uint8)
            save_image_array(image_array, file_name=file_name, ext="")
    return {
        "file_count":file_count,
        "filenames": filenames
    }

def start_server():
    uvicorn.run(app,port=8888,host="0.0.0.0")#,reload=True, debug=True)

if __name__=="__main__":
    # to run in debug mode
    # uvicorn server_template:app --reload --port 8888
    start_server()


