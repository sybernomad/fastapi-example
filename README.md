# fastapi-example
Skeleton code for fastapi.


# Run

* Clone
* `poetry install` 
* `poetry run python src/fastapi_example/app.py --help`

```
fastapi-example (main)> poetry run python src/fastapi_example/app.py --help
usage: app.py [-h] [--api_ip API_IP] [--api_port API_PORT]

Example description

options:
  -h, --help           show this help message and exit
  --api_ip API_IP      The IP the api will listen on. (default: 0.0.0.0)
  --api_port API_PORT  The port the API will listen on. (default: 8000)
```

* Run `poetry run python src/fastapi_example/app.py` and it will listen by default on http://0.0.0.0:8000.

* Navigate to http://0.0.0.0:8000/docs to play around with the two example endpoints.
