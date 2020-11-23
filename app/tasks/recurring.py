from app.task import registry
from app.logger import log


@registry.task(ignore_result=True)
def ring_in_the_new_year():
    log.info("Happy New Year!")
    return "ok"
