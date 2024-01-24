import os
import shutil

folder_path = 'C:/Users/vengann/Desktop/forTrain/coco128/images/train2017'  # Folder path

directory = os.listdir(folder_path)

# Counter for image index
image_index = 1

for item in directory:
    # Check if the item is a file (not a folder)
    if os.path.isfile(os.path.join(folder_path, item)):
        # Get the file extension
        _, file_extension = os.path.splitext(item)

        # Create the new file name
        new_name = f'image_{image_index}{file_extension}'

        # Construct the full source and destination paths
        source_path = os.path.join(folder_path, item)
        destination_path = os.path.join(folder_path, new_name)

        # Move the file to the new name (overwriting if it already exists)
        shutil.move(source_path, destination_path)

        # Increment the image index
        image_index += 1





























# import os

# source_folder = 'C:/Users/vengann/Desktop/forTrain/coco128/images/train2017'  # Source folder
# destination_folder = 'C:/Users/vengann/Desktop/train_Test/New folder/'  # Destination folder

# # Ensure the destination folder exists, create it if it doesn't
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

# directory = os.listdir(source_folder)

# # Counter for image index
# image_index = 1

# for item in directory:
#     # Check if the item is a file (not a folder)
#     if os.path.isfile(os.path.join(source_folder, item)):
#         # Get the file extension
#         _, file_extension = os.path.splitext(item)

#         # Create the new file name
#         new_name = f'image_{image_index}{file_extension}'

#         # Construct the full source and destination paths
#         source_path = os.path.join(source_folder, item)
#         destination_path = os.path.join(destination_folder, new_name)

#         # Rename the file
#         os.rename(source_path, destination_path)

#         # Increment the image index
#         image_index += 1
