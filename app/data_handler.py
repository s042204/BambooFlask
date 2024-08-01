import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dev.db')

def read_employees():
    df_employees = pd.read_sql('SELECT * FROM employees', engine)
    return df_employees
