from PIL import Image, ImageEnhance, ImageFilter
import os

# Define paths
path = "./images"
pathOut = "./editedImg"

# Check if the output directory exists; if not, create it
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Process each file in the input directory
for filename in os.listdir(path):
    print(f"Processing {filename}...")
    try:
        # Open the image file
        img = Image.open(f"{path}/{filename}")
        
        # Apply a SHARPEN filter and convert to grayscale
        edit = img.filter(ImageFilter.SHARPEN).convert("L")
        
        # Get the clean filename without extension
        clean_name = os.path.splitext(filename)[0]
        
        # Save the edited image to the output directory
        edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))
        print(f"Saved {clean_name}_edited.jpg")
        
    except Exception as e:
        print(f"Failed to process {filename}: {e}")
