from pydantic import BaseModel
from typing import Optional

class TriageAction(BaseModel):
    category: str
    priority: str
    action_type: str
    folder: Optional[str] = None
    reply_draft: Optional[str] = None
    forward_to: Optional[str] = None
