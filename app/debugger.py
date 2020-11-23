import debugpy

from app.config import settings


def start():
    if settings.DEBUGGING_ENABLED:
        # 5678 is the default attach port in the VS Code debug configurations.
        # Unless a host and port are specified, host defaults to 127.0.0.1
        debugpy.listen(5678)
        print("Waiting for debugger to attach...")
        debugpy.wait_for_client()
        debugpy.breakpoint()
