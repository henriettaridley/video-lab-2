import os
from PIL import Image, ImageDraw, ImageFont
from collections import OrderedDict

def create_image_grid(folder_path, output_filename, title=None, images_per_row=5, num_images_to_select=15):
    # Collect image filenames
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))]
    images.sort()  # Ensure images are in alphabetical/numerical order
    # Check if there are enough images for first and last 10, if not, take as many as possible up to 20, if less than that, take all
    if len(images) > 2 * num_images_to_select:
        images = images[50:50+num_images_to_select] # Select first and last 10 images only
    elif len(images) > 0:
        # Not enough images for 20, take all unique images
        images = list(OrderedDict.fromkeys(images[:num_images_to_select]))
    else:
        print(f"No images found in {folder_path}. Skipping grid creation.")
        return
    
    # Load images
    loaded_images = [Image.open(img) for img in images]
    if not loaded_images:
        print(f"No images found or they could not be loaded from {folder_path}.")
        return

    num_images = len(loaded_images)  # Update the number of images as we have picked only 20
    
    widths, heights = zip(*(i.size for i in loaded_images))
    max_width = max(widths)
    max_height = max(heights)
    
    num_rows = (num_images + images_per_row - 1) // images_per_row

    # Create the grid canvas
    grid_width = images_per_row * max_width
    grid_height = num_rows * max_height
    
    # Optional title addition
    title_height = 0
    if title:
        try:
            font = ImageFont.truetype('arial.ttf', size=20)  # Update with your local path to the font if necessary
        except IOError:
            font = ImageFont.load_default()
            
        title_width, title_height = font.getsize(title)
        title_height += 10  # Padding below the title
        grid_height += title_height
        
    grid_image = Image.new('RGB', (grid_width, grid_height), color='white')

    # Optionally draw the title
    if title:
        draw = ImageDraw.Draw(grid_image)
        draw.text(((grid_width - title_width) // 2, 5), title, font=font, fill="black")

    # Paste the images into the grid
    for index, image in enumerate(loaded_images):
        row = (index // images_per_row)
        col = index % images_per_row
        grid_image.paste(image, (col * max_width, row * max_height + title_height))

    # Save the grid image
    grid_image.save(output_filename)


# Example usage
def create_grids_for_folders(base_folder):
    for method_folder in os.listdir(base_folder):
        method_path = os.path.join(base_folder, method_folder)
        if os.path.isdir(method_path):
            for video_folder in os.listdir(method_path):
                video_path = os.path.join(method_path, video_folder)
                if os.path.isdir(video_path):
                    grid_filename = f"20_{video_folder}_{method_folder}_grid.jpg"
                    grid_file_path = os.path.join(base_folder, '/grid_images/', grid_filename)  # Save in the base folder
                    title = f"{video_folder} ({method_folder})"
                    create_image_grid(video_path, grid_file_path, title=title)

# Set your base directory here
create_grids_for_folders("mega.pytorch/visualization")


# Create the images for the initial method
image_path = "mega.pytorch/visualization"
# Create the 'grid_images' directory if it does not exist
os.makedirs(os.path.join(image_path, 'grid_images'), exist_ok=True)

grid_filename = f"15_image_path_grid.jpg"
# The corrected line:
grid_file_path = os.path.join(image_path, 'grid_images', grid_filename)  # Save in the base folder, without the starting slash
title = image_path  # The title can be the same as the folder path or any other title you wish to give
create_image_grid(image_path, grid_file_path, title=title)