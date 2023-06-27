"""importing modules"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.jwt import auth_handler
from core.jwt.auth_bearer import JWTBearer
from core.database.connection import get_db
from .crud import (
    get_user_by_email,
    verify_email_password,
    get_password,send_email
    )
from .schema import login

router = APIRouter()

@router.post("/email_login", tags=["employees"])
def employee_login(user:login, user_db:Session=Depends(get_db)):
    """employee login"""
    check_user = get_user_by_email(db=user_db, email=user.Email)
    if not check_user:
        raise HTTPException(
            status_code=404,
            detail={
                "status" : "Error",
                "status_code" : 404,
                "data" : None,
                "error" : {
                    "status_code":404,
                    "status":'Error', 
                    "Message" : "Email not found!"
                }
            }
        )
    verify_password = verify_email_password(db=user_db, email=user.Email, password=user.Password)
    if not verify_password:
        raise HTTPException(
        status_code=401,
        detail={
            "status" : "Error",
            "status_code" : 401,
            "data" : None,
            "error" : {
                "status_code":401,
                "status":'Error', 
                "Message1" : "Login failed! Invalid credentials"
            }
        }
        )
    access_token = auth_handler.encode_token(user.Email)
    refresh_token = auth_handler.refresh_token(user.Email)
    response_msg = {
                        "detail": {
                            "status": "Success",
                            "status_code": 200,
                            "data": {
                                "status_code": 200,
                                "status": "Success",
                                "message": "Login successfully",
                                "access_token": access_token, "token_type": "bearer",
                                "refresh_token": refresh_token, "token_type": "bearer",
                                "email": user.Email,
                            },
                            "error": None
                        }
                    }
    return response_msg
@router.post("/forgot_password", tags=["employees"])
async def forgot_password(email: str, user_db:Session=Depends(get_db)):
    """forgot password"""
    check_user = get_user_by_email(db=user_db, email=email)
    if not check_user:
        raise HTTPException(
            status_code=404,
            detail={
                "status" : "Error",
                "status_code" : 404,
                "data" : None,
                "error" : {
                    "status_code":404,
                    "status":'Error', 
                    "Message" : "Email not found!"
                }
            }
        )
    fetch_password = get_password(db=user_db, email=email)
    send_otp = send_email(sender_email = "sruthivania@gmail.com" ,
                        #   sender_password="",
                        sender_password = "qtbdjyilopaxvsmi",

                        receiver_email = email ,
                        subject = "your password has been sent",
                        message = fetch_password
                         )
    if send_otp:
        response_msg = {
                        "detail": {
                            "status": "Success",
                            "status_code": 200,
                            "data": {
                                "status_code": 200,
                                "status": "Success",
                                "message": "OTP has sent to the registered email",
                                "password":fetch_password
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
                "Message1" : "failed to send OTP"
                }
            }
        )    
@router.get("/employees_profile", tags=["employees"])
async def profile(token = Depends(JWTBearer()), user_db : Session = Depends(get_db)):
    """ fetching employee profile"""
    token = auth_handler.decode_token(token=token)
    user = get_user_by_email(user_db, token['sub'])
    response_msg = {
        "detail" :{
            "status":"Success",
            "status_code":200,
            "data":{
                "status_code":200,
                "status":"Success",
                "message":"Profile fetched successfully",
                "fullname": user.name,
                "employee_id":user.employee_id,
                "email":user.email,
                "designation": user.designation
            }
        }
    }
    return response_msg
