# seealso:
# https://airflow.apache.org/docs/docker-stack/index.html
# https://airflow.apache.org/docs/docker-stack/build.html#build-build-image

# The Apache Airflow community, releases Docker Images which are reference images for Apache Airflow.
# The community releases a production-ready reference container image
# Every time a new version of Airflow is released, the images are prepared in the apache/airflow DockerHub for all the supported Python versions.
# This repository uses an extending approach because the goal is to create a quick start
# To see the pros and cons between extending and customizing see https://airflow.apache.org/docs/docker-stack/build.html#extending-vs-customizing-the-image
FROM apache/airflow:2.4.0-python3.10 as dev_image

# Adding a new PyPI package
# RUN pip install --no-cache-dir lxml

# Adding new apt package
# When adding packages via apt you should switch to the root user when running the apt commands, but do not forget to switch back to the airflow user after installation is complete.
#USER root
#RUN apt-get update \
#  && apt-get install -y --no-install-recommends \
#         vim \
#  && apt-get autoremove -yqq --purge \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/*

# with user root
# USER 0
# COPY docker/pycharm-interpreter.sh /pycharm-interpreter.sh
# RUN chmod 755 /pycharm-interpreter.sh

# switch back to the airflow user
USER airflow

# 8080 airflow webservice
EXPOSE 8080

