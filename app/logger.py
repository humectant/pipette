import sys
import logging

import structlog

from app.config import settings

level = settings.LOG_LEVEL
if "PRETTY" == settings.LOG_RENDERER:
    renderer = structlog.dev.ConsoleRenderer()
else:
    renderer = structlog.processors.JSONRenderer()

shared_processors = [
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
]

formatter = structlog.stdlib.ProcessorFormatter(
    processor=structlog.dev.ConsoleRenderer(), foreign_pre_chain=shared_processors,
)

structlog.configure(
    processors=shared_processors + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter,],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

formatter = structlog.stdlib.ProcessorFormatter(processor=renderer, foreign_pre_chain=shared_processors,)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handlers = [handler]

logging.basicConfig(level=level, handlers=handlers)

log = structlog.getLogger(__name__)
