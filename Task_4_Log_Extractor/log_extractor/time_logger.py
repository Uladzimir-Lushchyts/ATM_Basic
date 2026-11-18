import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)

def time_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        try:
            result = func(*args, **kwargs)

        finally:
            execution_time = time.perf_counter() - start_time
            logger.info(f"Execution time: {execution_time:.3f} seconds")

        return result

    return wrapper