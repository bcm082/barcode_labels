import os
from PIL import Image, ImageDraw, ImageFont
import cairosvg

def mm_to_pixels(mm, dpi=96):
    return int((mm / 25.4) * dpi)

input_directory = '/Users/bruno/Documents/bruno_dev/barcode_labels/svg_files'
output_directory = '/Users/bruno/Documents/bruno_dev/barcode_labels/svg_files'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith('.svg'):
        svg_path = os.path.join(input_directory, filename)
        output_image_path = os.path.join(output_directory, filename.replace('.svg', '.png'))

        cairosvg.svg2png(url=svg_path, write_to=output_image_path, dpi=300)

        image = Image.open(output_image_path)
        width, height = image.size

        font_size = 30
        font_path_regular = "/Library/Fonts/Arial.ttf"
        font_path_bold = "/Library/Fonts/Arial Bold.ttf"
        try:
            font_regular = ImageFont.truetype(font_path_regular, font_size)
            font_bold = ImageFont.truetype(font_path_bold, font_size)
        except IOError:
            print("Font path is not valid. Using default fonts.")
            font_regular = ImageFont.load_default()
            font_bold = font_regular

        new_width = max(width, 900)
        new_height = height + 170

        new_image = Image.new('RGB', (new_width, new_height), 'white')
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

        # Extract the SKU name from the filename
        sku_name = filename.split(" - ")[1].replace(".svg", "")  # Assumes format "UPC - SKU.svg"

        _, _, bottom_text_width, bottom_text_height = draw.textbbox((0, 0), sku_name, font=font_regular)
        bottom_text_x = (new_width - bottom_text_width) / 2
        bottom_text_y = new_height - bottom_text_height - 70
        draw.text((bottom_text_x, bottom_text_y), sku_name, font=font_regular, fill="black")
        
        _, _, bold_bottom_text_width, bold_bottom_text_height = draw.textbbox((0, 0), "MADE IN CHINA", font=font_bold)
        bold_bottom_text_x = (new_width - bold_bottom_text_width) / 2
        bold_bottom_text_y = bottom_text_y + bottom_text_height + 5
        draw.text((bold_bottom_text_x, bold_bottom_text_y), "MADE IN CHINA", font=font_bold, fill="black")

        new_image.save(output_image_path, compress_level=1)
        print(f"Image saved at {output_image_path}")

print("All files processed.")
