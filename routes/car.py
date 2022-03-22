# LIBS
from fastapi        import APIRouter
from fastapi        import Depends, HTTPException
from sqlalchemy.orm import Session

from client         import get_db, R
from models         import Car, CarResponse, CarRequest, Response


# SERVICE
CarService = APIRouter(
    prefix  = "/car",
    tags    = ["car"]
)

# Read
@CarService.get("/get/{id}", response_model=CarResponse)
async def get_car(id:int, db:Session=Depends(get_db)):
    # Process
    car = db.query(Car).filter(Car.id == id).first()
    if car is None:
        raise HTTPException(status_code=400, detail=Response(
            message="Failed To Find Car!",
            data=None
        ))
        
    # Response
    return CarResponse.from_orm(car)

@CarService.get("/", response_model=Response)
async def get_car_name(car_plate: str = "", db:Session=Depends(get_db)):
    # Process [Redis implementation]
    carPlate= car_plate.upper()
    carName = R.get(carPlate)

    if not carName:
        car = db.query(Car).filter(Car.car_plate == carPlate).first()
        if car is None:
            raise HTTPException(status_code=400, detail=Response(
                message="Failed To Find Car!",
                data=None
            ).dict())
        
        carName = car.car_name
        R.set(carPlate, carName); R.expire(carPlate, 600)

    # Response
    return Response(
        message="Succeed To Find Car!",
        data=carName
    )


# Write
@CarService.post("/create", response_model=CarResponse)
async def create_car(car:CarRequest, db:Session=Depends(get_db)):
    # Process
    car = car.to_model()
    db.add(car)
    db.commit()
    db.refresh(car)

    # Response
    return CarResponse.from_orm(car)