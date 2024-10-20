import pandas as pd
import os

# Function to clean the CSV file
def clean_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values; here we fill with the mean for numerical columns and 'Unknown' for object columns
    for column in df.columns:
        if column.strip() == 'Age':
            df[column].replace(' ','0', inplace=True)
        elif column.strip() == "City":
            df[column].replace(' ', 'Unknown', inplace=True)

    # Display cleaned data
    print("\nCleaned Data:")
    print(df)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    curPath = os.path.dirname(__file__)
    print(curPath)
    input_csv = os.path.join(curPath, "mock-data/mock-data.csv")
    output_csv = os.path.join(curPath, "mock-data/mock-data-out.csv")
    clean_csv(input_csv, output_csv)
