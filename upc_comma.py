# This script will take a csv file with a UPC column and separate each row by comma
import pandas as pd

def save_upcs_to_file(csv_file_path, output_file_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Extract the UPC column and convert it to a comma-separated string
    upc_string = ','.join(data['UPC'].astype(str))
    
    # Save the UPC string to a text file
    with open(output_file_path, 'w') as file:
        file.write(upc_string)

# Example usage:
# Replace 'path_to_your_csv.csv' with the path to your CSV file
# Replace 'path_to_your_output_file.txt' with the path where you want to save the output
save_upcs_to_file('Barcodes.csv', 'Barcodes.txt')
