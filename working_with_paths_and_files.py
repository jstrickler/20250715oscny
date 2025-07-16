import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")

print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")
print(f"{os.path.abspath(file_path) = }")

file_size = os.path.getsize(file_path)
print(f"{file_size = }")
raw_timestamp = os.path.getmtime(file_path)
print(f"{raw_timestamp = }")
file_mod_time = datetime.fromtimestamp(raw_timestamp)
print(f"{file_mod_time = }")
print(file_mod_time)
print(f"{os.path.exists(file_path) = }")
print(f"{os.path.exists('wombats.txt') = }")
print(f"{os.path.isdir(FOLDER) = }")
print(f"{os.path.isdir(file_path) = }")

print(f"{os.path.split(file_path) = }")
print(f"{os.path.splitext(file_path) = }")
print(f"{os.path.splitdrive(os.path.abspath(file_path)) = }")
