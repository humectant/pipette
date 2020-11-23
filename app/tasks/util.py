from typing import Optional

from app.logger import log
from app.task import registry
from app.tasks.core import PipTask


@registry.task(ignore_result=False)
def noop(*args, **kwargs):
    # Task accepts any arguments and does nothing
    log.info(f"noop: args={args} kwargs={kwargs}")
    return f"args={args} kwargs={kwargs}"


@registry.task(bind=True, base=PipTask, ignore_result=True, soft_time_limit=5, time_limit=10)
def fuget_about_it(self) -> str:
    message = "Fugetaboutit!"
    self._record(message)
    return message


@registry.task(bind=True, base=PipTask, ignore_result=True, soft_time_limit=5, time_limit=10)
def talk_to_me(self, word: Optional[str] = "Joe") -> str:
    message = f"Talk to me {word}!"
    self._record(message)
    return message
