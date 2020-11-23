from datetime import datetime
from typing import Optional, List, Any

import pendulum
from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[str] = None
    name: str
    args: List[Any] = []
    created: Optional[datetime] = pendulum.now()
    status: Optional[str] = "pending"

