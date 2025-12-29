import time

from fastapi import Request

from src.utils import log, ProjectException


async def log_middleware(request: Request, call_next):
    """ Middleware that logs the request and returns the response. """

    start_time = time.time()

    response = await call_next(request)
    duration = time.time() - start_time

    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'duration': duration,
    }
    log.info(log_dict)
    return response





