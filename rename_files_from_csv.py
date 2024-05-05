import pandas as pd
import os

def rename_svg_files(csv_file_path, svg_directory_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Create a dictionary to map UPC to SKU
    upc_to_sku = dict(zip(data['UPC'].astype(str), data['SKU']))
    
    # Check if the directory exists
    if not os.path.exists(svg_directory_path):
        print(f"Error: The directory {svg_directory_path} does not exist.")
        return
    
    # Get list of SVG files in the directory
    svg_files = [f for f in os.listdir(svg_directory_path) if f.endswith('.svg')]
    
    # Check if there are SVG files in the directory
    initial_count = len(svg_files)
    if not svg_files:
        print("No SVG files found in the directory.")
        return

    renamed_count = 0  # Counter for the number of files successfully renamed
    
    # Loop through each SVG file
    for filename in svg_files:
        # Extract UPC from the filename (remove the .svg part)
        upc = filename.split('.')[0]
        
        # Find the matching SKU
        if upc in upc_to_sku:
            # Replace invalid characters in filenames
            safe_sku = upc_to_sku[upc].replace('/', '-')
            
            # Create new filename with SKU
            new_filename = f"{upc} - {safe_sku}.svg"
            old_file_path = os.path.join(svg_directory_path, filename)
            new_file_path = os.path.join(svg_directory_path, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            renamed_count += 1  # Increment the counter for successfully renamed files
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Skipping file: No matching SKU found for UPC {upc} in the CSV file.")

    print(f"Total files initially: {initial_count}")
    print(f"Total files renamed: {renamed_count}")

# Example usage:
rename_svg_files('Barcodes.csv', '/Users/bruno/Documents/bruno_dev/barcode_labels/svg_files')
