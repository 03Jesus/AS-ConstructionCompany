from logic.models.person_model import PersonModel


class ClientModel (PersonModel):

    class Config:
        from_attributes = True


class ClientModelRespone (PersonModel):
    id: int

    class Config:
        from_attributes = True


class ClientUpdateModel (PersonModel):
    class Config:
        from_attributes = True
