# Task 02: Simple Image Encryption Tool

A command-line image encryption utility that performs pixel-level bitwise manipulation on image channels using the Python `Pillow` library.

## How it Works
The tool iterates over every pixel in the input image and applies a bitwise XOR (`^`) operation on the Red, Green, and Blue channels using a user-specified integer key (0-255). 

Because XOR is symmetric and self-inverting:
$$\text{Encrypted} = \text{Original} \oplus \text{Key}$$
$$\text{Decrypted} = \text{Encrypted} \oplus \text{Key} = \text{Original}$$

Running the exact same encryption script with the same key on the encrypted image perfectly restores the original image!

> [!IMPORTANT]
> **Use PNG for Encrypted Images**: 
> You must save the encrypted output in a lossless format like **PNG**. If you save the encrypted output as a lossy format (like **JPEG**), the color compression algorithms will alter the scrambled pixel values slightly, making perfect decryption impossible and leaving the decrypted image corrupted.

### Prerequisites
1. Python 3.x installed.
2. Install the **Pillow** library:
   ```bash
   pip install pillow
   ```

### How to Run
Execute the script from your terminal:
```bash
python image_encryptor.py
```
### Usage Example
1. Run the script and choose Option `1`.
2. Input image path: `my_photo.png`
3. Output image path: `encrypted_photo.png`
4. Key: `123`
5. The image is now encrypted and unviewable!
6. To decrypt, run the tool again on `encrypted_photo.png`, specify the output as `decrypted_photo.png`, and enter the same key `123`.

## Execution Result
Here is the execution demonstration showing the image pixel encryption process:

![Execution Result](Screenshot%202026-06-01%20094735.png)

"# SCT_CS_2" 
