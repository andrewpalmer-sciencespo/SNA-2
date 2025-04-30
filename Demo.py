from PIL import Image, ImageOps

# Open the image
image = Image.open("example.jpg")

# Add padding to center the image
centered_image = ImageOps.expand(image, border=(50, 50, 50, 50), fill='white')

# Save or display the centered image
centered_image.save("centered_example.jpg")