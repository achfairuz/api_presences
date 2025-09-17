from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from typing import Any, Optional
class ResponseStatus:
    @staticmethod
    def success(data, message="Data retrieved successfully", code=status.HTTP_200_OK):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "status": "success",
                "message": message,
                "data": data
            })
        )
        
    @staticmethod
    def update_success(data: Optional[Any] = None,
    message: str = "Data updated successfully",
    code: int = status.HTTP_200_OK):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "status": "success",
                "message": message,
                "data": data
            })
        )
    
    @staticmethod 
    def delete_success(
        message: str = "Data deleted successfully",
        code: int = status.HTTP_200_OK
    ):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "status": "success",
                "message": message,
                "data": None
            })
        )
        
    @staticmethod
    def success_create(  data: Optional[Any] = None,
    message: str = "Data created successfully",
    code: int = status.HTTP_201_CREATED):
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder({
                "status": "success",
                "message": message,
                "data": data
            })
        )
    
    @staticmethod
    def error(
        message: str = "An error occurred",
        debug: Optional[str] = None,
        code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder({
                "status": "error",
                "message": message,
                "debug": debug,   # bisa tampilkan error detail kalau diaktifkan
                "data": None
            })
        )
        
    @staticmethod
    def not_found(
        message: str = "Resource not found",
        code: int = status.HTTP_404_NOT_FOUND
    ):
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder({
                "status": "error",
                "message": message,
                "data": None
            })
        )