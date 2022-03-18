# LIBS
import config;  import client
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# MAIN APP
# ENV
config.env_load('.env')

# APP
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = config.origins.keys(),
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(routes.CarService)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)