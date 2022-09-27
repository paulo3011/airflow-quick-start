# seealso: https://airflow.apache.org/docs/docker-stack/build.html#build-build-image

FROM apache/airflow:2.4.0-python3.10 as dev_image

# Adding a new PyPI package
RUN pip install --no-cache-dir lxml

# Adding new apt package
# When adding packages via apt you should switch to the root user when running the apt commands, but do not forget to switch back to the airflow user after installation is complete.
#USER root
#RUN apt-get update \
#  && apt-get install -y --no-install-recommends \
#         vim \
#  && apt-get autoremove -yqq --purge \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/*

# switch back to the airflow user
USER airflow

# 8080 airflow webservice
EXPOSE 8080

