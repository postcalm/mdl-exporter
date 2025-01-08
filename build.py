import os
import subprocess
from itertools import count


ROOT_DIR = os.getcwd()
PROJECT_NAME = "export_mdl"
COUNTER = count(0)
TEMPL_NAME = f"{PROJECT_NAME}{{}}.zip"

zip_name = TEMPL_NAME.format(next(COUNTER))
zip_path = os.path.join(ROOT_DIR, zip_name)


while True:
    try:
        os.unlink(zip_name)
        break
    except FileNotFoundError:
        zip_name = TEMPL_NAME.format(next(COUNTER))
    except PermissionError:
        zip_name = TEMPL_NAME.format(next(COUNTER))
        break


subprocess.run(["7z", "a", "-mx5", "-mmt=6", f"{zip_name}", f"{PROJECT_NAME}"])
print("NEW NAME:", zip_name)
