# airflow-quick-start

To start:

```shell
cd docker
docker-compose up --build
```

To clear:
```shell
cd docker
docker-compose down
```

Setup venv

```shell
pip list
# Package    Version
# ---------- -------
# pip        22.2.2
# setuptools 60.2.0
# wheel      0.37.1
```

```shell
source venv/bin/activate
AIRFLOW_VERSION=2.4.0
PYTHON_VERSION="3.10"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[psycopg2]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}" --no-cache-dir -v
```

If "error: metadata-generation-failed" on install psycopg2, try this:

```shell
sudo apt install libpq-dev python3-dev
# https://stackoverflow.com/questions/35104097/how-to-install-psycopg2-with-pg-config-error
```
or 

seealos: https://stackoverflow.com/questions/70961915/error-while-installing-pytq5-with-pip-preparing-metadata-pyproject-toml-did-n (--use-deprecated=backtrack-on-build-failures
)

# to setup envs:

```shell
export $(grep -v '^#' /home/paulo/projects/paulo3011/airflow-quick-start/docker/airflow-env-variables.env | xargs)
```

# References

- https://www.astronomer.io/blog/7-common-errors-to-check-when-debugging-airflow-dag/
- https://www.astronomer.io/guides/debugging-dags/
- https://bobcares.com/blog/docker-exec-format-error/
- https://docs.docker.com/compose/compose-file/compose-file-v3/
- https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
- https://github.com/apache/airflow/blob/v2-4-stable/IMAGES.rst
- https://airflowsummit.org/slides/j2-Ensuring-your-DAGs-work-before-going-to-production.pdf
- https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#staging-environment