import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from an Excel file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Check for missing values
        missing_values = data.isnull().sum()
        if missing_values.sum() > 0:
            print("Missing Values:")
            print(missing_values)
        else:
            print("No missing values found.")

        # Display summary statistics
        print("\nSummary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("\nHistograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()

def main():
    file_path = input("Enter the path to the Excel file: ")
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()



