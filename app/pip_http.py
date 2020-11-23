import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

DEFAULT_TIMEOUT = 60


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


caller = requests.Session()
adapter = TimeoutHTTPAdapter(
    max_retries=Retry(
        total=3,
        backoff_factor=10,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS", "POST"],
    )
)
caller.mount("https://", adapter)
caller.mount("http://", adapter)
