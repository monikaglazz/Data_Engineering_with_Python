from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta


# ex 1 "Executor implications"
report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *"
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2020, 2, 20),
    mode='reschedule',
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2020, 2, 20),
    dag=report_dag
)

precheck >> generate_report_task


#   ex 2 "Defining an SLA"
# Create the dictionary entry
default_args = {
    'start_date': datetime(2020, 2, 20),
    'sla': timedelta(minutes=30)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args,
               schedule_interval='@None')


# ex 3 "Defining a task SLA"
test_dag2 = DAG('test_workflow', start_date=datetime(
    2020, 2, 20), schedule_interval='@None')

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag2)


# ex 4 "Generate and email a report"
# Define the email task
email_report = EmailOperator(
    task_id='email_report',
    to='airflow@datacamp.com',
    subject='Airflow Monthly Report',
    html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
    files=['monthly_report.pdf'],
    dag=report_dag
)

# Set the email task to run after the report is generated
email_report << generate_report


# ex 5 "Adding status emails"
# Setup email alerting for the success and failure cases
default_args = {
    'email': ["airflowalerts@datacamp.com", "airflowadmin@datacamp.com"],
    'email_on_failure': True,
    'email_on_success': True
}

report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *",
    default_args=default_args
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2020, 2, 20),
    mode='reschedule',
    dag=report_dag)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2020, 2, 20),
    dag=report_dag
)

precheck >> generate_report_task
