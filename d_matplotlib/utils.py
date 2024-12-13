import pandas
import inspect

def extract_entities(data):
    columns = data.columns.tolist()
    return columns

def extract_args(function):
    return inspect.signature(function)

    
