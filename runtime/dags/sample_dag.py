from datetime import datetime, timedelta
from airflow import DAG
from airflow.executors.debug_executor import DebugExecutor
from airflow.operators.empty import EmptyOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 10, 2),
    "depends_on_past": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "email_on_retry": False
}

dag = DAG("sample_dag",
          default_args=default_args,
          description="Sample dag.",
          # https://crontab.guru/#0_3_*_*_*
          # schedule="0 3 * * *",
          schedule="0 1 * * *",
          catchup=False,
          start_date=default_args["start_date"]
          )

start_operator = EmptyOperator(task_id="Begin_execution", dag=dag)
end_operator = EmptyOperator(task_id="Stop_execution", dag=dag)

start_operator >> end_operator


def debug_dag(dag: DAG, use_default_executor=False):
    """Debug a DAG in with DebugExecutor not needing to change airflow.cfg."""
    dag.clear()

    if use_default_executor:
        dag.run()
    else:
        dag.run(executor=DebugExecutor())


if __name__ == "__main__":
    from airflow.utils.state import State

    debug_dag(dag)
