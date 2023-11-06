import os
# Directory containing the image files
image_directory = 'sample_data/images'
# Get a list of image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
print(image_files)
# New file name prefix
new_filename_prefix = 'new_image_'
# Rename the image files
for i, image_file in enumerate(image_files, start=1):
    current_file_path = os.path.join(image_directory, image_file)
    new_filename = f"{new_filename_prefix}{i}.jpg"  # You can change the file extension if needed
    new_file_path = os.path.join(image_directory, new_filename)
    # Check if the current file exists before renaming
    if os.path.exists(current_file_path):
        try:
            # Rename the file
            os.rename(current_file_path, new_file_path)
            print(f'Renamed {current_file_path} to {new_file_path}')
        except Exception as e:
            print(f'Error renaming file: {str(e)}')
    else:
        print(f'File {current_file_path} does not exist')