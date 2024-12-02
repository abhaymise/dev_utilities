import hashlib
import shutil
import traceback
from datetime import datetime
from pathlib import Path


def copyDir(SOURCE, BACKUP):
    try:
        shutil.copytree(SOURCE, BACKUP)
    except Exception as error:
        traceback.print_exc()
        return Path(BACKUP)
    return Path(BACKUP)


def doesFileExist(file_path):
    return Path(file_path).exists()


def getCreationTime():
    """
    returns string and datetime.datetime object
    """
    from datetime import datetime
    now = datetime.now()  # current date and time
    day_name_format = "%a %b %d %H:%M:%S %Y"
    day_num_format = "%m/%d/%Y, %H:%M:%S"
    date_time = now.strftime(day_num_format)
    return date_time


def getuniquehashcode():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.encode('utf-8')
    hash = hashlib.sha1()
    hash.update(dt_string)
    version = hash.hexdigest()
    return version, dt_string
