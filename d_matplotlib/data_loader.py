import pandas as pd

def load_data(file_path):
    """_summary_

    Args:
        file_path (string): actual file path

    Returns:
        data (class): readable pandas array
    """
    # grab file format by regular expression
    file_format = file_path.split('.')[-1].lower()
    
    # convert to pandas dataframe
    try:
        if file_format == 'csv':
            data = pd.read_csv(file_path)
            return data
        elif file_format == 'excel' or file_path == 'xlsx':
            data = pd.read_excel(file_path)
            return data
        elif file_format == 'json':
            data = pd.read_json(file_path)
            return data
        elif file_format == 'txt':
            try:
                data = pd.read_csv(file_path, delimiter= ',')
            except:
                data = pd.read_csv(file_path, delimiter= '\t')
            return data
        else:
            print("upload the correct format file")
            
    except Exception as e:
        print(f"Error loading data: {e}")   