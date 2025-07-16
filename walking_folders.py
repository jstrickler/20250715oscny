import os

START_FOLDER = "."

for folder, subs, files in os.walk(START_FOLDER):
    if '.git' in subs:
        subs.remove('.git')
    # print(folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f"{file_size:6d} {file_name}")
