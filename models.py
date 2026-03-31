from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict, Any
from uuid import uuid4

class EmailObservation(BaseModel):
    email_id: str
    subject: str
    sender: str
    body_snippet: str
    timestamp: str
    thread_id: Optional[str] = None
    sender_reputation: float = Field(0.0, ge=0.0, le=1.0)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class TriageAction(BaseModel):
    category: Literal["work", "personal", "spam", "urgent", "promo"]
    priority: Literal["high", "medium", "low"]
    action_type: Literal["archive", "reply", "forward", "route_to_folder", "escalate_to_human", "noop"]
    folder: Optional[str] = None
    reply_draft: Optional[str] = None
    forward_to: Optional[str] = None

class TriageState(BaseModel):
    episode_id: str = Field(default_factory=lambda: str(uuid4()))
    step_count: int = 0
    emails_processed: int = 0
    task_name: str = "easy"
    attention_budget_remaining: int = 5
