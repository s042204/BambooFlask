from flask import Blueprint, jsonify, session, redirect, url_for
from app import db
import os
import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

auth_bp = Blueprint('auth', __name__)
employees_bp = Blueprint('employees', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login route"}), 200

@employees_bp.route('/employees', methods=['GET'])
def get_employees():
    from app.models import Employees
    # if not session.get('logged_in'):
    #     return redirect(url_for('auth.login'))

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

        for api_employee in api_employees:
            if not Employees.query.filter_by(id=api_employee['id']).first():
                new_employee = Employees(
                    id=api_employee['id'],
                    display_name=api_employee.get('displayName', 'N/A'),
                    job_title=api_employee.get('jobTitle', 'N/A'),
                    work_phone_extension=api_employee.get('workPhoneExtension', ''),
                    department=api_employee.get('department', 'Unknown'),
                    supervisor=api_employee.get('supervisor', '')
                )
                db.session.add(new_employee)

        db.session.commit()

        return jsonify({"message": "Employees data updated"}), 200

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return jsonify({"error": "Failed to fetch employees from API"}), 500
    except Exception as err:
        print(f"An error occurred: {err}")
        return jsonify({"error": "An unexpected error occurred"}), 500
