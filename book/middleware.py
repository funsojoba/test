import logging
import time


logger = logging.getLogger("django.request")

class LogRequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()
        
        try:
            response = self.get_response(request)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
            logger.error(f"Error processing request: {e}")
            raise
        finally:
            end_time = time.time()
            request_time = end_time - start_time
            # Time taken: 0.123s, Status: 200.
            logger.info(f"Time taken: {request_time:.3f}s, Status: {status_code}.")
            return response