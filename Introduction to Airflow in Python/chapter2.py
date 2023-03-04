# Import the DAG object
from airflow.models import DAG
# Import the BashOperator
from airflow.operators.bash import BashOperator
# Import the PythonOperator
from airflow.operators.python import PythonOperator
# Import the Operator
from airflow.operators.email import EmailOperator
# import datetime
from datetime import datetime, timedelta
# import requests library
import requests
# import json library
import json

# ex 1 "Defining a BashOperator task"
analytics_dag = DAG('test_dag', default_args={
                    'start_date': datetime(2020, 1, 1, 0, 0, 0)})

# Define the BashOperator
cleanup = BashOperator(
    task_id='cleanup_task',
    # Define the bash_command
    bash_command='cleanup.sh',
    # Add the task to the dag
    dag=analytics_dag
)


# ex 2  "Multiple BashOperators"
# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=analytics_dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=analytics_dag)


# ex 3 "Define order of BashOperators"
# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json',
    dag=analytics_dag
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data


# ex 4 "Using the PythonOperator"
def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")


process_sales_dag = DAG('process_sales', default_args={
                        'owner': 'sales_eng', 'start_date': datetime(2020, 2, 1, 0, 0, 0)})

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL': 'http://dataserver/sales.json',
               'savepath': 'latestsales.json'},
    dag=process_sales_dag
)


# ex 5 "More PythonOperators"
def parse_file(inputfile, outputfile):
    with open(inputfile) as infile:
        data = json.load(infile)
        with open(outputfile, 'w') as outfile:
            json.dump(data, outfile)


# Add another Python task
parse_file_task = PythonOperator(
    task_id='parse_file',
    # Set the function to call
    python_callable=parse_file,
    # Add the arguments
    op_kwargs={'inputfile': 'latestsales.json',
               'outputfile': 'parsedfile.json'},
    # Add the DAG
    dag=process_sales_dag
)


# ex 6 "EmailOperator and dependencies"
# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task


# ex 7 "Schedule a DAG via Python"
# Update the scheduling arguments as defined
default_args = {
    'owner': 'Engineering',
    'start_date': datetime(2019, 11, 1),
    'email': ['airflowresults@datacamp.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args,
          schedule_interval='30 12 * * 3')
