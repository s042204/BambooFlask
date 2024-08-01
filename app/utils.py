import os
import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError 

load_dotenv()

def fetch_employees_from_bamboohr():
    url = os.getenv('BAMBOOHR_API_URL')
    api_token = os.getenv('BAMBOOHR_API_TOKEN')
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Basic {api_token}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 

        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return None
