# Main

from data_extraction import extract_data, test_extract_data
from data_transformation import transform_data, test_transform_data
from data_loading import load_data, test_load_data

# Orchestrate ETL pipeline

def main():
    # Extract data
    data = extract_data()
    test_extract_data()
    
    # Transform data
    transformed_data = transform_data(data)
    test_transform_data()
    
    # Load data
    load_data(transformed_data)
    test_load_data()
    
if __name__ == '__main__':
    main()