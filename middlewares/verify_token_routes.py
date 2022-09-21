from typing import Callable
from typing import Callable
from fastapi import Request, Response
from functions_jwt import validate_token
from fastapi.routing import APIRoute

class VerifyTokenRoutes(APIRoute):
    def get_route_hanlder(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def verify_token(request: Request)-> Response:
            validate_response=validate_token(request.headers['Authorization'], output=False)
            
            if validate_response == None:
                response : Response = await original_route_handler(request)
                return response
            else:
                return validate_response
            
        return verify_token