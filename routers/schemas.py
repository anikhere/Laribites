from pydantic import BaseModel

class Vendor(BaseModel):
    name: str
    phone: str
    location: str
    availability: bool