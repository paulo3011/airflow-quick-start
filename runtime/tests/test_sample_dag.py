import datetime
import unittest

import pendulum
from airflow.executors.debug_executor import DebugExecutor
from airflow.models import DAG, DagBag, TaskInstance
from airflow.operators.bash import BashOperator
from airflow.utils.state import DagRunState, TaskInstanceState
from airflow.utils.types import DagRunType


class SampleDagTest(unittest.TestCase):
    """
    seealso: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
    """
    dag_bag = None
    dag_id = "sample_dag"

    def setUp(self) -> None:
        self.dag_bag = DagBag()
        self._clear_dag(self.dag_id)

    def _getDag(self) -> DAG:
        return self.dag_bag.get_dag(dag_id=self.dag_id)

    def test_dag_loaded(self):
        """
        Unit tests ensure that there is no incorrect code in your DAG. You can write unit tests for both your tasks and your DAG
        :return: None
        """
        dag = self.dag_bag.get_dag(dag_id=self.dag_id)
        assert self.dag_bag.import_errors == {}
        assert dag is not None
        assert len(dag.tasks) == 2

    def test_task_execution(self):
        """
        Unit tests to ensure that tasks perform as expected
        :return: None
        """
        dag = self._getDag()

        data_interval_start = pendulum.datetime(2022, 9, 14, tz="UTC")
        data_interval_end = data_interval_start + datetime.timedelta(days=1)

        dagrun = dag.create_dagrun(
            state=DagRunState.RUNNING,
            execution_date=data_interval_start,
            data_interval=(data_interval_start, data_interval_end),
            start_date=data_interval_end,
            run_type=DagRunType.MANUAL,
            run_id=f'test_{pendulum.now().isoformat()}',
            external_trigger=True
        )

        task = dag.get_task(task_id="Begin_execution")
        ti = TaskInstance(task, data_interval_start)
        ti.run(ignore_ti_state=True)  # test_mode=True
        assert ti.state == TaskInstanceState.SUCCESS
        # Assert something related to tasks results.

        task = dag.get_task(task_id="Stop_execution")
        ti = TaskInstance(task, data_interval_start)
        # ti.task = task
        # ti.render_templates()
        ti.run(ignore_ti_state=True)
        assert ti.state == TaskInstanceState.SUCCESS
        # Assert something related to tasks results.

    def _clear_dag(self, dag_id):
        """
        Delete all DB records related to the specified DAG.
        seealso: https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#delete_repeat1
        :param dag_id:
        :return: None
        """
        from airflow.utils.context import Context
        dag = DAG(
            "clear_dag",
            schedule=None,
            start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
            catchup=False,
        )

        parameterized_task = BashOperator(
            task_id="clear_dag_task",
            bash_command=f"airflow dags delete -y {dag_id}",
            dag=dag,
        )
        context = Context()
        parameterized_task.execute(context=context)
