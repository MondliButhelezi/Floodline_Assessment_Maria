from PIL import Image
import os

# Increase the decompression bomb limit
Image.MAX_IMAGE_PIXELS = None

# Define paths
image_path = "data/Map_Extent_Satellite_0.png"  # Path to the large image
output_dir = "data/slices"  # Directory to store the split images
os.makedirs(output_dir, exist_ok=True)

# Open the large image
if not os.path.exists(image_path):
    print(f"Error: The image path '{image_path}' does not exist.")
    exit(1)

img = Image.open(image_path)

# Define slice size (e.g., 1024x1024 pixels)
slice_width = 1024
slice_height = 1024

# Get image dimensions
img_width, img_height = img.size
print(f"Image dimensions: {img_width}x{img_height}")

# Split the image into smaller chunks
for i in range(0, img_width, slice_width):
    for j in range(0, img_height, slice_height):
        # Define the bounding box (left, upper, right, lower)
        box = (i, j, min(i + slice_width, img_width), min(j + slice_height, img_height))
        chunk = img.crop(box)

        # Save each chunk
        chunk_name = f"{output_dir}/chunk_{i}_{j}.png"
        chunk.save(chunk_name)
        print(f"Saved: {chunk_name}")

print("Image splitting complete!")
