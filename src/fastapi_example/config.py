from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_ip: str = Field(description="The IP the api will listen on.", default="0.0.0.0")
    api_port: int = Field(description="The port the API will listen on.", default=8000)
