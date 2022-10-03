import datetime
import unittest

import pendulum
from airflow.executors.debug_executor import DebugExecutor
from airflow.models import DAG, DagBag, TaskInstance
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

        try:
            dagrun = dag.create_dagrun(
                state=DagRunState.SUCCESS,
                execution_date=data_interval_start,
                data_interval=(data_interval_start, data_interval_end),
                start_date=data_interval_end,
                run_type=DagRunType.MANUAL,
                run_id=f'test_{pendulum.now().isoformat()}',
                external_trigger=True
            )
        except:
            print("dag run already exists")

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
