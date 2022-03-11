import shutil
import traceback
from pathlib import Path
from PIL import Image
import hashlib

def check_image_with_pil(path):
    try:
        PIL.Image.open(path)
    except IOError:
        print(f"[ERROR] there is a problem opening the image : {path}")
        return -1
    return 1
  
def copyDir(SOURCE,BACKUP):
  try:
      shutil.copytree(SOURCE, BACKUP)
  except Exception as error:
      traceback.print_exc()
      return Path(BACKUP)
  return Path(BACKUP)

def verifyImage(dataset_root):
  for c in dataset_root.ls():
    print(f"cleaning dir {c}")
    verify_images(c,delete=True,max_size=500)

def doesFileExist(file_path):
    return Path(file_path).exists()

def getCreationTime():
    """
    returns string and datetime.datetime object
    """
    from datetime import datetime
    now = datetime.now() # current date and time
    day_name_format = "%a %b %d %H:%M:%S %Y"
    day_num_format = "%m/%d/%Y, %H:%M:%S"
    date_time = now.strftime(day_num_format)
    return date_time

def getuniquehahcode():
    from datetime import datetime
    import hashlib
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.encode('utf-8')
    hash = hashlib.sha1()
    hash.update(dt_string)
    version = hash.hexdigest()
    return version,dt_string 
