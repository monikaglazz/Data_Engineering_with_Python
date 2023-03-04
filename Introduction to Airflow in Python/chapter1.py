# Import the DAG object
from airflow.models import DAG
# import datetime 
from datetime import datetime



# ex 1
# create first DAG
# Define the default_args dictionary
default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2020, 1, 14),
  'retries': 2
}

# Instantiate the DAG object
etl_dag = DAG('example_etl', default_args=default_args)