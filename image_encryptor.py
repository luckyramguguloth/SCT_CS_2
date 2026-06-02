"""
Task 02: Simple Image Encryption Tool
SkillCraft Technology Cybersecurity Internship
This script implements a simple image encryption and decryption utility using 
pixel-level bitwise XOR manipulation. It utilizes the Pillow library for image handling.
"""

import sys
import os

try:
    from PIL import Image
except ImportError:
    print("[!] Error: The 'Pillow' library is required to run this script.")
    print("    Please install it using: pip install pillow")
    sys.exit(1)

def process_image(input_path: str, output_path: str, key: int):
    if not os.path.exists(input_path):
        print(f"[!] Error: The file '{input_path}' does not exist.")
        return False
    try:
        byte_key = key % 256
        
        print(f"[*] Opening image: {input_path}")
        with Image.open(input_path) as img:
            # We convert the image to RGBA (or RGB) to easily manipulate pixel channels
            original_mode = img.mode
            has_alpha = 'A' in original_mode
            
            target_mode = "RGBA" if has_alpha else "RGB"
            converted_img = img.convert(target_mode)
            # Load pixel data
            pixels = converted_img.load()
            width, height = converted_img.size
            print(f"[*] Processing {width}x{height} pixels using bitwise XOR key {byte_key}...")
            # Loop through all coordinates and apply XOR operation to RGB channels
            for x in range(width):
                for y in range(height):
                    pixel_data = pixels[x, y]
                    
                    if target_mode == "RGBA":
                        r, g, b, a = pixel_data
                        # Apply XOR key to color channels, leave transparency channel intact
                        pixels[x, y] = (r ^ byte_key, g ^ byte_key, b ^ byte_key, a)
                    else:
                        r, g, b = pixel_data
                        pixels[x, y] = (r ^ byte_key, g ^ byte_key, b ^ byte_key)
            
            # Save the processed image
            print(f"[*] Saving processed image to: {output_path}")
            ext = os.path.splitext(output_path)[1].lower()
            if ext in ('.jpg', '.jpeg'):
                print("[!] WARNING: Saving encrypted images as JPEG (lossy) can degrade/alter")
                print("    pixel values due to compression, preventing perfect decryption.")
                print("    It is highly recommended to save output as lossless PNG format.")
                
            converted_img.convert(original_mode).save(output_path)
            print("[+] Processing complete successfully!")
            return True
            
    except Exception as e:
        print(f"[!] An error occurred during image processing: {e}")
        return False


def print_banner():
    """Prints a styled terminal banner."""
    print("=" * 60)
    print("              SIMPLE IMAGE ENCRYPTOR/DECRYPTOR                 ")
    print("=" * 60)

def main():
    print_banner()
    while True:
        try:
            print("\nOptions:")
            print("1) Encrypt/Decrypt an Image (Symmetric XOR)")
            print("2) Exit")
            choice = input("Select an option (1-2): ").strip()
            
            if choice == '2':
                print("\nGoodbye!")
                break
            if choice != '1':
                print("[!] Invalid option. Please enter 1 or 2.")
                continue
            input_path = input("\nEnter the path to the input image file: ").strip()
            input_path = input_path.strip('"').strip("'")
            
            output_path = input("Enter the path for the output image file: ").strip()
            output_path = output_path.strip('"').strip("'")
            
            key_input = input("Enter an integer key (0-255): ").strip()
            try:
                key = int(key_input)
            except ValueError:
                print("[!] Invalid key. Key must be an integer.")
                continue
            process_image(input_path, output_path, key)
        except (KeyboardInterrupt, EOFError):
            print("\n\nOperation cancelled. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
