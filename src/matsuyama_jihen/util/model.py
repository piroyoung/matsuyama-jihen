from pydantic import BaseModel
import uuid
import time


class ExampleMessage(BaseModel):
    id: str
    body: str
    created_at: int

    @classmethod
    def of_body(cls, body: str) -> "ExampleMessage":
        return cls(id=str(uuid.uuid4()), body=body, created_at=int(time.time()))
