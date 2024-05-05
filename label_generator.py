from PIL import Image, ImageDraw, ImageFont
import cairosvg

def mm_to_pixels(mm, dpi=96):
    # Convert millimeters to inches (1 inch = 25.4 mm) and then to pixels
    return int((mm / 25.4) * dpi)

# SVG and output paths
svg_path = '123456789012.svg'
output_image_path = '123456789012.png'

# Convert SVG to PNG using cairosvg with higher DPI
cairosvg.svg2png(url=svg_path, write_to=output_image_path, dpi=300)

# Open the generated PNG
image = Image.open(output_image_path)
width, height = image.size

# Define Fonts
font_size = 30  # Font size for both regular and bold text
font_path_regular = "/Library/Fonts/Arial.ttf"  # Regular font path
font_path_bold = "/Library/Fonts/Arial Bold.ttf"  # Bold font path

try:
    font_regular = ImageFont.truetype(font_path_regular, font_size)
    font_bold = ImageFont.truetype(font_path_bold, font_size)
except IOError:
    print("One of the specified font paths is not valid. Using default fonts.")
    font_regular = ImageFont.load_default()  # Fallback to default font
    font_bold = font_regular  # Use the same default font if bold is not found

# Adjust the image size if necessary (increase width for address and height for text)
new_width = max(width, 900)  # Ensure the canvas is wide enough for the address
new_height = height + 170  # Adjust height to prevent overlap

# Create a new image with adjusted size
new_image = Image.new('RGB', (new_width, new_height), 'white')

# Center the barcode horizontally and vertically
barcode_x_position = (new_width - width) // 2
barcode_y_position = (new_height - height) // 2
new_image.paste(image, (barcode_x_position, barcode_y_position))

draw = ImageDraw.Draw(new_image)

# Calculate text positions and draw texts
# 'textbbox' returns a tuple (left, top, right, bottom)
_, _, top_text_width, top_text_height = draw.textbbox((0, 0), "COSTUME AGENT", font=font_bold)
top_text_x = (new_width - top_text_width) / 2
top_text_y = 5
draw.text((top_text_x, top_text_y), "COSTUME AGENT", font=font_bold, fill="black")

_, _, second_text_width, second_text_height = draw.textbbox((0, 0), "3160 RIDGEWAY CT, COMMERCE TWP - MI - 48390 - USA", font=font_regular)
second_text_x = (new_width - second_text_width) / 2
second_text_y = top_text_y + top_text_height + 5
draw.text((second_text_x, second_text_y), "3160 RIDGEWAY CT, COMMERCE TWP - MI - 48390 - USA", font=font_regular, fill="black")

_, _, bottom_text_width, bottom_text_height = draw.textbbox((0, 0), "TESTSKU001", font=font_regular)
bottom_text_x = (new_width - bottom_text_width) / 2
bottom_text_y = new_height - bottom_text_height - 70
draw.text((bottom_text_x, bottom_text_y), "TESTSKU001", font=font_regular, fill="black")

_, _, bold_bottom_text_width, bold_bottom_text_height = draw.textbbox((0, 0), "MADE IN CHINA", font=font_bold)
bold_bottom_text_x = (new_width - bold_bottom_text_width) / 2
bold_bottom_text_y = bottom_text_y + bottom_text_height + 5
draw.text((bold_bottom_text_x, bold_bottom_text_y), "MADE IN CHINA", font=font_bold, fill="black")

# Save the new image with adjusted quality settings
new_image.save(output_image_path, compress_level=1)
print(f"Image saved at {output_image_path}")
