from PIL import Image
import os

# Change size for all image files
source_folder = 'C:/Users/vengann/Desktop/train_Test/images/train/'  # infinity folder
destination_folder = 'C:/Users/vengann/Desktop/train_Test/New folder/'  # new folder for all resized images

# Ensure the destination folder exists, create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

directory = os.listdir(source_folder)

# Counter for image index
image_index = 1

for item in directory:
    # Check if the item is a file (not a folder)
    if os.path.isfile(os.path.join(source_folder, item)):
        img = Image.open(os.path.join(source_folder, item))
        width, height = img.size
        ratio = width / height
        new_width = 640
        new_height = min(int(new_width / ratio), 640)  # Set new_height to the minimum of calculated height and 640

        try:
            # Attempt to use ANTIALIAS attribute (Pillow)
            img_resize = img.resize((new_width, new_height), Image.ANTIALIAS)
        except AttributeError:
            # If the attribute is not available, use BICUBIC filtering (common alternative)
            img_resize = img.resize((new_width, new_height), Image.BICUBIC)

        # Save the resized image with a name like "image_1.jpg", "image_2.jpg", etc.
        img_resize.save(os.path.join(destination_folder, f'image_{image_index}.jpg'), quality=100)

        # Increment the image index
        image_index += 1
