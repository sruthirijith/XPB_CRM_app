"""imporying modules"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database.connection import get_db
from .schema import merchant_details
from .crud import (check_if_merchant_email_exist,
                   create_merchant_profile,
                   check_if_gstin_number_exist,
                   check_if_website_exist,
                   check_if_gst_exist,
                   check_if_tan_exist,
                #    send_otp,
                #    verify_both_otp
                   )

router = APIRouter()

@router.post("/add_merchant", tags=["Merchant"])
async def add_merchant( merchant : merchant_details, user_db: Session = Depends(get_db)):
    """add merchant"""
    merchant_profile = check_if_merchant_email_exist(db = user_db, email=merchant.email)
    if merchant_profile:
        raise HTTPException (
                    status_code = 409,
                    detail = {
                        "status":"Error",
                        "status_code" : 409,
                        "data" : None,
                        "error" : {
                            "status":"Error",
                            "status_code" : 409,
                            "message" : "Merchant email already exist"
                        }
                    }
                )
    merchant_gstin_details = check_if_gstin_number_exist(db=user_db ,
                                                         gstin_number=merchant.gstin_number)
    if merchant_gstin_details:
        raise HTTPException (
                    status_code = 409,
                    detail = {
                        "status":"Error",
                        "status_code" : 409,
                        "data" : None,
                        "error" : {
                            "status":"Error",
                            "status_code" : 409,
                            "message" : "Merchant gstin number already exist"
                        }
                    }
                )
    merchant_website = check_if_website_exist(db=user_db, website=merchant.website)
    if merchant_website:
        raise HTTPException (
            status_code = 409,
            detail = {
                        "status":"Error",
                        "status_code" : 409,
                        "data" : None,
                        "error" : {
                            "status":"Error",
                            "status_code" : 409,
                            "message" : "Merchant website already exist"
                        }
                    }
                )
    merchant_gst = check_if_gst_exist(db=user_db, gst_number=merchant.gst_number)
    if merchant_gst:
        raise HTTPException (
                    status_code = 409,
                    detail = {
                        "status":"Error",
                        "status_code" : 409,
                        "data" : None,
                        "error" : {
                            "status":"Error",
                            "status_code" : 409,
                            "message" : "gst number already exist"
                        }
                    }
                )
    merchant_tan = check_if_tan_exist(db=user_db, tan_number=merchant.tan_number)
    if merchant_tan:
        raise HTTPException (
                    status_code = 409,
                    detail = {
                        "status":"Error",
                        "status_code" : 409,
                        "data" : None,
                        "error" : {
                            "status":"Error",
                            "status_code" : 409,
                            "message" : "tan number already exist"
                        }
                        }
                    )
    create_merchant_info = create_merchant_profile(db=user_db, merchant= merchant)
    # submit_otp = send_otp(registered_number=merchant.contact_number)
    if create_merchant_info:
        response_msg = {
                "detail": {
                "status": "Success",
                "status_code": 201,
                    "data": {
                    "status_code": 201,
                    "status": "Success",
                    "message": "Merchant information submitted Successfully",
                    # "otp"    : submit_otp
                  },
                "error": None
            }
        }   
        return response_msg
    raise HTTPException(
    status_code=409,
    detail={
            "status" : "Error",
            "status_code" : 409,
            "data" : None,
            "error" : {
                "status_code":409,
                "status":'Error', 
                "Message1" : "failed to submit merchant information"
                 }
        }
    )    
# @router.post("/verify_otp", tags=["Merchant"])
# async def verify_otp(otp_received: str):
#     """verify otp"""
#     check_otp = verify_both_otp(otp1=otp_received)
#     if check_otp:
#         response_msg = {
#                 "detail": {
#                 "status": "Success",
#                 "status_code": 201,
#                     "data": {
#                     "status_code": 201,
#                     "status": "Success",
#                     "message": "OTP has verified , merchant onboarded successfully"
#                 },
#                 "error": None
#             }
#         }   
#         return response_msg
#     raise HTTPException(
#             status_code = 404,
#             detail = {
#                 "status": "Error",
#                 "status_code" : 404,
#                 "data": None,
#                 "error" : {
#                     "status_code" : 404,
#                     "status":"Error",
#                     "message" : "Wrong OTP enterd, please try again.",
#                 }
#             },
#         )    
