from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
from process import process_data

default_args = {
    'start_date': datetime(2019, 1, 1),
    'sla': timedelta(minutes=90)
}

dag = DAG(dag_id='etl_update', default_args=default_args)


sensor = FileSensor(task_id='sense_file',
                    filepath='/Data_Engineering_with_Python\Introduction to Airflow in Python/startprocess.txt',
                    poke_interval=45,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles',
                         bash_command='rm -f /Data_Engineering_with_Python\Introduction to Airflow in Python/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing',
                             python_callable=process_data,
                             provide_context=True,
                             dag=dag)


email_subject = """
  Email report for {{ params.department }} on {{ ds_nodash }}
"""


email_report_task = EmailOperator(task_id='email_report_task',
                                  to='sales@mycompany.com',
                                  subject=email_subject,
                                  html_content='',
                                  params={
                                      'department': 'Data subscription services'},
                                  dag=dag)


no_email_task = EmptyOperator(task_id='no_email_task', dag=dag)


def check_weekend(**kwargs):
    dt = datetime.strptime(kwargs['execution_date'], "%Y-%m-%d")
    # If dt.weekday() is 0-4, it's Monday - Friday. If 5 or 6, it's Sat / Sun.
    if (dt.weekday() < 5):
        return 'email_report_task'
    else:
        return 'no_email_task'


branch_task = BranchPythonOperator(task_id='check_if_weekend',
                                   python_callable=check_weekend,
                                   provide_context=True,
                                   dag=dag)


sensor >> bash_task >> python_task

python_task >> branch_task >> [email_report_task, no_email_task]
