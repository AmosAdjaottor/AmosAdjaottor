
import cv2

def sketch_image(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_gray = 255 - gray_image
    
    # Apply Gaussian Blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred_image
    
    # Create the sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    
    # Save the sketch
    cv2.imwrite(output_path, sketch)

if __name__ == "__main__":
    input_path = "C:/Users/hossa/OneDrive/Pictures/mouse.jpg"
    output_path = "C:/Users/hossa/OneDrive/Pictures/mouse_sketch.jpg"
    sketch_image(input_path, output_path)
