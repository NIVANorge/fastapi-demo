# FastAPI demo 

Demo code written as live-coding during section meeting 2020-02-13. 
The demo showcases API-development using FastAPI.

## getting started

### dependencies

- python3 with pip

### install

```
pip install -r requirements.txt
cd src
python main.py
```


## fastapi
- "flask-like" code
- uvicorn - lightning-fast ASGI server
  - Asynchronous Server Gateway Interface
  - async IO successor to WSGI (Web Server Gateway Interface)
- uvloop 
  - alternative to asyncio event loop
- pydantic
  - data validation
  - used to generate JSON schema/openapi spec
- openapi
  - automatic documentation
  - allows clientside code generation (ymmv)

