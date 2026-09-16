import os
import glob
from PIL import Image

image_dir = r"C:\Users\user\Desktop\Karu\landing_preview\Imagenes"
html_files = [
    r"C:\Users\user\Desktop\Karu\landing_preview\index.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html"
]

def optimize_images():
    # Read HTML contents
    html_contents = {}
    for hf in html_files:
        if os.path.exists(hf):
            with open(hf, 'r', encoding='utf-8') as f:
                html_contents[hf] = f.read()
    
    # Process all images
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        for filepath in glob.glob(os.path.join(image_dir, ext)):
            filename = os.path.basename(filepath)
            name, current_ext = os.path.splitext(filename)
            
            # Skip already optimized
            if current_ext.lower() == '.webp':
                continue
                
            new_filename = name + ".webp"
            new_filepath = os.path.join(image_dir, new_filename)
            
            print(f"Processing {filename}...")
            
            try:
                with Image.open(filepath) as img:
                    # Convert to RGB if necessary (WebP supports RGBA but let's be safe for JPEG)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGBA")
                    elif img.mode != "RGB":
                        img = img.convert("RGB")
                    
                    # Resize if too large
                    max_size = 1920
                    if max(img.size) > max_size:
                        ratio = max_size / max(img.size)
                        new_size = (int(img.width * ratio), int(img.height * ratio))
                        # Use LANCZOS for high quality downsampling
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                    # Save as WebP
                    img.save(new_filepath, "WEBP", quality=82, method=6)
                
                # If successful, replace in HTMLs
                for hf in html_contents:
                    # URL encoded paths might be used, but in our HTML they are just spaces
                    html_contents[hf] = html_contents[hf].replace(filename, new_filename)
                    # Also handle URL encoded just in case
                    import urllib.parse
                    encoded_filename = urllib.parse.quote(filename)
                    encoded_new = urllib.parse.quote(new_filename)
                    html_contents[hf] = html_contents[hf].replace(encoded_filename, encoded_new)
                    
                # Delete original
                os.remove(filepath)
                print(f"Optimized {filename} to {new_filename}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
    # Write updated HTML
    for hf, content in html_contents.items():
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
            
if __name__ == "__main__":
    optimize_images()
