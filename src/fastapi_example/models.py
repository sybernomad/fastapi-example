from pydantic import BaseModel


class ExampleResp(BaseModel):
    """Example Response Model"""

    message: str

    model_config = {"json_schema_extra": {"examples": [{"detail": "Hello, World!"}]}}


class ExampleReq(BaseModel):
    """Example Request Model"""

    message: str

    model_config = {"json_schema_extra": {"examples": [{"message": "Hello, World!"}]}}
