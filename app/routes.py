from flask import Blueprint, jsonify
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from app.data_handler import read_employees

load_dotenv()

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees', methods=['GET'])
def fetch_and_store_employees():
    """Fetch employees from BambooHR API and store in database."""
    url = os.getenv('BAMBOOHR_API_URL')
    token = os.getenv('BAMBOOHR_API_TOKEN')

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Basic {token}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        api_employees = response.json().get('employees', [])

        df_employees = pd.DataFrame(api_employees)

        employees_list = read_employees().to_dict(orient='records')
        return jsonify(employees_list), 200

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return jsonify({"error": "Failed to fetch employees from API"}), 500
    except Exception as err:
        print(f"An error occurred: {err}")
        return jsonify({"error": "An unexpected error occurred"}), 500
