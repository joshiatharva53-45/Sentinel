"""
=========================================================
Task System
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Task:

    name: str

    payload: dict = field(default_factory=dict)

    priority: int = 0

    completed: bool = False

    created_at: datetime = field(default_factory=datetime.now)

    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))