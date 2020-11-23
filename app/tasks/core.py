from celery import Task

from app.logger import log


class PipTask(Task):
    """
    Celery base task with hooks for various task phases
    """
    _synthetic = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        log.error(f"{task_id} failed: {exc}")

    def on_success(self, retval, task_id, args, kwargs):
        pass

    def _record(self, data):
        log.info(f"Record task: {data}")


class RetryableException(Exception):
    """
    Exception that can be retried
    """
    pass


class IgnorableException(Exception):
    """
    Exception that can be ignored
    """
    pass
