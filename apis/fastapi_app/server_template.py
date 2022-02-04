from fastapi import FastAPI,Request
import numpy as np
import cv2
from pathlib import Path
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

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


def time_function(func):
    pass

@app.get("/")
def whoami():
    return f" hi am {app_name}"

@app.get("/form")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/files/")
async def create_file(file: bytes | None = File(None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}
"""
Using UploadFile has several advantages over bytes:
You don't have to use File() in the default value of the parameter.
It uses a "spooled" file:
A file stored in memory up to a maximum size limit, and after passing this limit it will be stored in disk.
This means that it will work well for large files like images, videos, large binaries, etc. without consuming all the memory.
You can get metadata from the uploaded file.
https://fastapi.tiangolo.com/tutorial/request-files/
"""

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
"""
Multiple File Uploads¶
It's possible to upload several files at the same time.
They would be associated to the same "form field" sent using "form data".
"""
@app.post("/files/")
async def create_files(files: list[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

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


