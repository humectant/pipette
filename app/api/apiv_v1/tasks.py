from typing import Any

from fastapi import APIRouter

from app.logger import log
from app.schemas import utils
from app.task import registry

router = APIRouter()


@router.post("/task", status_code=201)
def run_task(
    task: utils.Task,
) -> Any:
    """
    Execute Celery task
    """
    log.info(f"Run task {task}")
    task_id = registry.send_task(task.name, args=task.args)
    task.id = str(task_id)
    task.status = "sent"
    return task

