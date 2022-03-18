# LIBS
from sqlalchemy     import Column, Boolean, ForeignKey, Integer, String
from typing         import Optional
# DB
from client.mysql   import Base
from pydantic       import BaseModel


# MODEL DB
class Car(Base):
    __tablename__ = "cars"
    id          = Column(Integer, primary_key=True, index=True)
    car_name    = Column(String(50), index=True)
    car_plate   = Column(String(50), index=True)


# SCHEMAS
class CarResponse(BaseModel):
    id:         Optional[str] = None
    car_name:   str
    car_plate:  str

    class Config:
        orm_mode = True

class CarRequest(BaseModel):
    car_name:   str
    car_plate:  str

    def to_model(self) -> Car:
        return Car(
            car_name = self.car_name,
            car_plate= self.car_plate
        )