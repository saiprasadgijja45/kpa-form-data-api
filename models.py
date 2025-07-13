from pydantic import BaseModel
from typing import Optional

# Input model (used in POST request)
class FormData(BaseModel):
    full_name: str
    email: str
    phone: str
    state: Optional[str] = None
    district: Optional[str] = None

# Output model (used in responses)
class FormDataResponse(FormData):
    id: int
