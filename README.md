pipette
===========

Provides APIs via FastAPI/Starlette and task execution via Celery. Requires Python 3.8 and Docker.

A single Docker image is used for APIs and task workers. docker-compose is used to simulate a 
production environment with the following services:
- api: Exposes an HTTP API
- worker: Celery workers
- rabbitmq: Standard RabbitMQ image; Celery broker
- redis: Standard Redis image; Celery backend

If you do not require a Celery backend, either unset CELERY_BACKEND or use in Python 
task decorators like this `ignore_result=True`.

#### Configure & Install
Create a .env file aat the top level of the project. To start out simply 
copy `.env.example` to `.env`. That will be sufficient to run the project locally and exceute the tests. 
```
pipenv run install
```

#### Start services
Start services in the background
```
docker-compose up -d
```
Tail the logs
```
docker-compose logs -f
```

The following endpoints are available:
- API: http://localhost/
- API Spec: http://localhost/docs
- RabbitMQ management: http://localhost:15672 (log in as guest/guest)

Ping
```
curl http://localhost/
```

Run a task via HTTP
```
curl --request POST \
  --url http://localhost/task \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "app.tasks.util.talk_to_me"
}'
```

## Testing
Run tests with docker-compose:
```
pipenv run local-test
```
This will bring down, build and start everything.

If your containers are already running, you can run the tests with:
```
docker-compose exec -T api bash /app/app/tests-start.sh
```

Enter a running container
```
docker-compose exec api /bin/bash
```

## Also See

- [Development](DEVELOPMENT.md)
- [IDE](IDE.md)
- [Celery](https://docs.celeryproject.org)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)