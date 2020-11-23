import newrelic.agent

from app.config import settings


def report(event, data):
    newrelic.agent.record_custom_event(settings.NEW_RELIC_EVENT_NAMESPACE, dict(event=event, **data))
