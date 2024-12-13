import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        columns = data.columns.tolist()
        print("Data Loaded Successfully!")

    except pd.errors.ParserError:
        try:
            data = pd.read_excel(file_path)
            columns = data.columns.tolist()
            print("Data Loaded Successfully!")

        except pd.errors.ParserError:
            try:
                data = pd.read_json(file_path)
                columns = data.columns.tolist()
                print("Data Loaded Successfully!")

            except pd.errors.ParserError:
            try:
                data = pd.read_json(file_path)
                columns = data.columns.tolist()
                print("Data Loaded Successfully!")
                
            except Exception as e:
                print(f"Error loading data: {e}")
                return None

    return data




    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'excel':
        return pd.read_excel(file_path)
    elif file_format == 'json':
        return pd.read_json(file_path)
    elif file_format == 'sql':
        # Assuming you have a SQL database connection already set up
        # Replace 'your_connection_string' with the actual connection string
        connection_string = 'your_connection_string'
        query = f"SELECT * FROM your_table_name;"
        return pd.read_sql(query, con=connection_string)