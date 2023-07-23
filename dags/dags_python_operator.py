from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 7, 11, tz="Asia/Seoul"),
    catchup=False
) as dag: