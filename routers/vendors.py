from fastapi import APIRouter
from fastapi import Request,HTTPException
from routers.schemas import Vendor
router = APIRouter()
vendors_db = {}
@router.get('/bhaji',tags=['bhaji'])
async def get_bhaji():
    return 'getting bhaji ok'
@router.get('/fruits',tags=['fruits'])
async def get_fruits():
    return 'getting fruits ok'
@router.get('/pulses',tags=['pulses'])
async def get_pulses():
    return 'getting pulses ok'
@router.get('/beans',tags=['beans'])
async def get_beans():
    return 'getting beans alright'
@router.post('/vendors')
async def Get_Vendor(vendor:Vendor):
     vendor_obj = vendor
     vendors_db[len(vendors_db)+1] = vendor_obj
     return vendors_db
@router.get('/vendors_get/{vendor_id}')
async def get_vendor_by_id(vendor_id:int):
    if vendor_id in vendors_db:
        vendor = vendors_db[vendor_id]
        return vendor
    else:
        raise HTTPException(status_code=404, detail="Vendor not found")
