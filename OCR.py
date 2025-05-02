# Required imports
import os
from PIL import Image
import pytesseract as pt

# Use absolute paths to avoid permission issues
# Change these paths to locations where you have write permissions
current_directory = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_directory, "test_images")
output_folder = os.path.join(current_directory, "extracted_texts")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List of image files in the directory
try:
    if os.path.exists(image_folder):
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    else:
        print(f"Image folder not found: {image_folder}")
        print("Creating the folder now. Please add your images to this folder.")
        os.makedirs(image_folder, exist_ok=True)
        image_files = []
except Exception as e:
    print(f"Error accessing image folder: {e}")
    image_files = []

# Function to extract text from image and save to .txt file
def extract_text_and_save(image_path, langs=["eng", "hin"]):
    try:
        image = Image.open(image_path)
        text = pt.image_to_string(image, lang='+'.join(langs)).strip()

        # Generate corresponding .txt filename
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        txt_file_path = os.path.join(output_folder, f"{base_name}.txt")

        # Write extracted text to file
        with open(txt_file_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"[✓] Extracted and saved: {txt_file_path}")
    except Exception as e:
        print(f"[!] Failed for {image_path}: {e}")

# Process all images in folder
print(f"Looking for images in: {image_folder}")
print(f"Saving extracted text to: {output_folder}")

if not image_files:
    print("No image files found in the specified directory.")
else:
    print(f"Found {len(image_files)} image(s) to process.")
    for image_file in image_files:
        full_path = os.path.join(image_folder, image_file)
        extract_text_and_save(full_path)