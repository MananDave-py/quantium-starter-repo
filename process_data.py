import csv
import os

# Define the folder where our original daily sales Excel/CSV files are stored
input_dir = 'data'

# Define the name of the final cleaned output file we will create
output_file = 'formatted_data.csv'

# Set up the names of the columns (headers) that we want in our final dataset
header = ['sales', 'date', 'region']

# Open our completely new output file in 'write' mode (this creates the file if it doesn't exist)
# We use newline='' to prevent blank rows from appearing between data rows in Windows
with open(output_file, 'w', newline='') as outfile:
    # Create a writer object that knows how to write data in CSV format
    writer = csv.writer(outfile)
    
    # Write our column names (sales, date, region) as the very first row
    writer.writerow(header)
    
    # Loop over every file name inside the 'data' directory
    for filename in os.listdir(input_dir):
        # We only want to process files that are CSVs, so we check the extension
        if filename.endswith(".csv"):
            # Construct the full path to the file (e.g., 'data/daily_sales_data_0.csv')
            filepath = os.path.join(input_dir, filename)
            
            # Open the individual input CSV file in 'read' mode
            with open(filepath, 'r') as infile:
                # DictReader reads the CSV and turns each row into a dictionary 
                # where the keys are the column names (product, price, quantity, date, region)
                reader = csv.DictReader(infile)
                
                # Examine each row in this file one by one
                for row in reader:
                    # We are only interested in tracking sales for "pink morsel", so we filter our data
                    if row['product'] == 'pink morsel':
                        # The price comes in as a string like "$3.00". 
                        # We must remove the dollar sign ('$') and convert it into a decimal number (float)
                        price = float(row['price'].replace('$', ''))
                        
                        # The quantity is a string (e.g. "546"), we convert it into a whole number (integer)
                        quantity = int(row['quantity'])
                        
                        # Multiply price by quantity to find out the total sales amount
                        sales = price * quantity
                        
                        # Simply extract the date and region directly from the row
                        date = row['date']
                        region = row['region']
                        
                        # Finally, save our calculated sales alongside the date and region 
                        # into our new formatted_data.csv file
                        writer.writerow([sales, date, region])

# Print a friendly message to the terminal once all files are successfully merged and processed!
print(f"Data processing complete. Saved to {output_file}")
