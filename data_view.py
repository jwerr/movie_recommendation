import pandas as pd

# Path to the CSV file
filepath = "data/movies.csv"

# Load the CSV file into a DataFrame
try:
    data = pd.read_csv(filepath)
    print("CSV file loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{filepath}' was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the CSV file: {e}")
    exit()

# Display the contents of the CSV file
print("\nContents of the CSV file:")
print(data)

# Optional: Display the first few rows of the CSV file
print("\nFirst 5 rows of the CSV file:")
print(data.head())

# Optional: Display basic information about the CSV file
print("\nBasic information about the CSV file:")
print(data.info())

# Optional: Display column names
print("\nColumn names in the CSV file:")
print(data.columns.tolist())