from fastapi import FastAPI, Depends, APIRouter
from app.interfaces.device_controller import DeviceController
from app.schemas.device_schema import DeviceResponse, DeviceCreate
from routes.API.dependencies import get_device_controller

router = APIRouter()

@router.post("/devices", response_model=DeviceResponse)
def create_device(device: DeviceCreate, controller: DeviceController = Depends(get_device_controller)):
    return controller.create_device(device)

@router.get("/devices/{device_id}", response_model=DeviceResponse)
def get_device(device_id: int, controller: DeviceController = Depends(get_device_controller)):
    return controller.get_device(device_id)

@router.get("/devices", response_model=list[DeviceResponse])
def get_devices(controller: DeviceController = Depends(get_device_controller)):
    return controller.get_devices()


@router.put("/devices/{device_id}", response_model=DeviceResponse)
def update_device(device_id: int, device: dict, controller: DeviceController = Depends(get_device_controller)):
    return controller.update_device(device_id, device)  

@router.delete("/devices/{device_id}", response_model=dict)
def delete_device(device_id: int, controller: DeviceController = Depends(get_device_controller)):
    return controller.delete_device(device_id)