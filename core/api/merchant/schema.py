import json
from typing import List
from sqlalchemy import Column,String,Date,Enum,DECIMAL

from pydantic import BaseModel, Field, EmailStr
from decimal import Decimal

from fastapi import UploadFile
from datetime import date
from core.models.mixin import GenderType


class merchant_details(BaseModel):

    merchant_name : str| None = Field(default = None, description = "Name of the store")   
    authorized_person :str= Field(default = None, description = "Authorized person")
    contact_number :str | None = Field(default = None, description = "store contact number")
    email         : EmailStr= Field(default = None, description = " email address")   
    dob           : date= Field(description = "Date Of Birth")
    gender : GenderType | None = Field(default=1, description="Gender 1-FEMALE, 2-MALE, 3-OTHER")
    merchant_upi_id : str = Field(default = None, description = "")
    percentage_of_commission_offered : Decimal | None = Field(default = None, description = "")
    gstin_number :str| None = Field(default = None, description = "GST document url")
    registered_shop_name : str= Field(..., description = "shop name")
    corporate_or_registration_name : str= Field(..., description = "shop name")
    website : str = Field(default = None, description = "website url")
    shop_category : str= Field(1, description = "category id")
    business_structure : str | None = Field(default=None, description="sole proprietorship, partnership, company, franchise")
    in_charge :str | None = Field(default = None, description = " staff profile id")
    business_phone_number : str = Field(default = None, description = "store contact number")
    address1 : str = Field(..., description = "store address")
    address2 : str = Field(default = None, description = "store secondary address")
    postal_code : str = Field(...,description = "PIN number")
    city : str = Field(..., description = "store's city")
    district : str = Field(..., description = "store's district")
    state : str = Field(..., description = "store's state")
    local_bodies : str = Field(default = None, description = "panchayath,muncipality,...")
    upload_shop_photo : str = Field(default = None, description = "Store images")   
    name_on_pan : str | None = Field(default = None, description = "PAN Holder Name")
    pan_number : str | None = Field(default = None, description = "PAN Card Number")
    gstin_number: str  | None = Field(default = None, description = "GST document url")
    tan_number : str  | None = Field(default = None, description = "TAN document url")
    gst_number :  str | None = Field(default = None, description = "GST document url")
    kyc_doc_type : int  | None = Field(default = None, description = "id proofs table id")
    kyc_doc_front : str  | None = Field(default = None, description = "KYC front document url")
    kyc_doc_back : str  | None = Field(default = None, description = "KYC back document url")
    upload_pan :  str = Field(default = None, description = "Store images")   
    

