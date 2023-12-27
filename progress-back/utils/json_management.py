import os
import json

def read(path:str):
    """
    Read and load JSON content from a file.

    Parameters:
    - path (str): The path to the JSON file.

    Returns:
    - dict: A Python dictionary containing the parsed JSON data.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - json.JSONDecodeError: If the JSON decoding fails.
    """

    try:
        with open(path, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file '{path}' was not found.") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding JSON in file '{path}'.") from e

def write(path:str, data:dict) -> None:
    """
    Write JSON data to a file.

    Parameters:
    - path (str): The path to the file where the JSON data will be written.
    - data (dict): The dictionary containing the data to be written to the file.

    Returns:
    - None

    Raises:
    - FileNotFoundError: If the specified file path is not found.

    Note:
    The function will overwrite the content of the file if it already exists.
    """

    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file path '{path}' was not found.") from e

def is_correct_database(path: str, expected_structure: dict) -> bool:
    """
    Check if the specified database file has the expected structure.

    Parameters:
    - path (str): The path to the database file.
    - expected_structure (dict): The expected structure of the database file.

    Returns:
    - bool: True if the file exists and has the expected structure, False otherwise.
    """
    # Check if the file exists
    if os.path.exists(path):
        try:
            # Read the content of the JSON file
            with open(path, 'r') as file:
                data = json.load(file)

            # Check if the expected structure is present
            if all(key in data and data[key] == expected_structure[key] for key in expected_structure):
                print("The database file exists and has the expected structure.")
                return True
            else:
                print("The database file does not have the expected structure.")
                return False
        except json.JSONDecodeError as e:
            print(f"JSON decoding error in the file '{path}': {e}")
            return False
    else:
        print("The database file does not exist.")
        return False

