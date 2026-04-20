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
@router.put('/vendors_update/{pre}',tags=['Put Method'])
async def update_vendors(pre:int,new_id:Vendor):
    if pre in vendors_db:
        vendors_db[pre] = new_id
        return vendors_db
    else:
        raise HTTPException(status_code=404, detail="Vendor not found")
@router.delete('/vendors_delete/{v_id}',tags=['delete method'])
async def delete_vendors(v_id:int):
    if v_id in vendors_db:
        del vendors_db[v_id]
        return vendors_db
    else:
        raise HTTPException(status_code=404, detail="Vendor not found")

            

