import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("sanket28/fitpulse-wearable-device-data-csv")

print("Path to dataset files:", path)

# Copy files to the current directory
current_dir = os.getcwd()
print(f"Copying files to: {current_dir}")

for file_name in os.listdir(path):
    full_file_name = os.path.join(path, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, current_dir)
        print(f"Copied {file_name}")
