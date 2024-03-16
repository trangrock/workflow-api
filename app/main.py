from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ping, routes
from app.api.constants import API_PREFIX

# Initialize the FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(ping.router)
app.include_router(routes.router, prefix=API_PREFIX)
