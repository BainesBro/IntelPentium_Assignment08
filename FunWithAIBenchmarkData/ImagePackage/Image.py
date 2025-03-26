from PIL import Image

def open_image(image_path):
    """Opens and returns an image."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def display_image(img):
    """Displays the image."""
    if img:
        img.show()

def main():
    """Main function to run the display logic."""
    image_path = (r"C:\Users\bainesct\source\repos\IntelPentium_Assignment08\IntelPentium.jpg")  # Replace with your image path
    img = open_image(image_path)
    display_image(img)