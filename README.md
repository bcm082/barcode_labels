# Simple script to create barcode labels

1. Install the required packages
```pip install -r requirements.txt```

2. Genereate the barcode in svg format go to https://barcodeqrcodegenerator.streamlit.app to generate a barcode.

3. Change the the variables to draw the text: Company Name, Address, SKU, Made in China

The script will generate a label ready to print and stick to the product.

Option to do in bulk run ```bulk_label_generator.py```

Example:
The program takes a SVG barcode and turn into a PNG label barcode with company info.
---
![Barcode](123456789012.svg)
---
![Label](123456789012.png)