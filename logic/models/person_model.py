from typing import Optional

from pydantic import BaseModel


class PersonModel (BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    mail: Optional[str]
