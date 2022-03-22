# LIBS
import config;  import client
import routes
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# MAIN APP
# APP
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        'http://localhost:3000',
        'http://192.168.0.4:3000',
        # NGINX [React]
        'http://localhost:80'
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(routes.CarService)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)