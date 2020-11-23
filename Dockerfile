FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

# Install pipenv, use it w/o a venv and then uninstall
# Curl just for testing
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pipenv install --deploy --system --dev; else pipenv install --deploy --system; fi"

COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./bin/start-reload.sh /start-reload.sh
COPY ./bin/start.sh /start.sh
RUN chmod +x /start.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
