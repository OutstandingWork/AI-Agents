import chardet

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        # Read some bytes from the file. You might need to adjust the sample size.
        raw_data = file.read(5000)
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        return encoding

# Example usage
file_path = 'TSLA.csv'
encoding = detect_csv_encoding(file_path)
print(f"The detected encoding is: {encoding}")