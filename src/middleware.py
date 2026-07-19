from fastapi import FastAPI
from fastapi.requests import Request
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

def register_middleware(app:FastAPI):
    @app.middleware('http')
    async def custom_logging(request:Request, call_next):
        start_time = time.time()
        print("before",start_time)
        respose = await call_next(request)
        processing_time = time.time() - start_time
        print("after processing",processing_time)
        return respose
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers= ['*'],
        allow_credentials= True,
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=['*'],
    )