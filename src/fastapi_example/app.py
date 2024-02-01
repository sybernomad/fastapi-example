import uvicorn
from fastapi import FastAPI

from fastapi_example.config import Settings
from fastapi_example.models import ExampleReq, ExampleResp
from fastapi_example.utils import make_parser

app = FastAPI(title="Example")


@app.get("/api/get_example", tags=["Example"])
async def get_example() -> ExampleResp:
    """Get example description."""
    return ExampleResp(message="Hello, World!")


@app.post("/api/post_example", tags=["Example"])
async def post_example(request: ExampleReq) -> ExampleResp:
    """Post example description."""
    return ExampleResp(message=request.message)


def main():
    parser = make_parser()
    args = vars(parser.parse_args())
    settings = Settings(**args)
    uvicorn.run(app, host=settings.api_ip, port=settings.api_port)


if __name__ == "__main__":
    main()
