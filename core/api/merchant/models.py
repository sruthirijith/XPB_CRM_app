from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum, DECIMAL, ARRAY, Text
from sqlalchemy.orm import relationship
from pydantic import Field

from core.database.connection import Base
from core.models.mixin import GenderType


# class BusinessCategory(Base):

#     __tablename__ = "business_category"
#     id = Column(Integer, primary_key = True)
#     category = Column(String(50), unique = True, nullable = False)


class MerchantInfo(Base): 

    __tablename__ = "merchant_profile_info"
    id                             = Column(Integer, primary_key=True)
    merchant_name                  = Column(String(50), nullable=False)
    authorized_person              = Column(String(50), nullable=True)
    contact_number                 = Column(String(20), nullable=False, unique=True)
    email                          = Column(String(100), nullable=False, unique=True)
    dob                            = Column(Date, nullable=True)
    gender                         = Column(Enum(GenderType), nullable=False) #1=f, 2=m
    merchant_upi_id                 = Column(String(50), nullable=True)
    percentage_of_commission_offered =Column(DECIMAL, nullable = True)
 

class MerchantBusinessInfo(Base):

    __tablename__ = "merchant_business_info"
    id                             = Column(Integer, primary_key=True)
    merchant_id                    = Column(Integer, ForeignKey("merchant_profile_info.id"), unique = True, nullable = False)
    gstin_number                   =Column(String(1024), nullable=False)
    registered_shop_name           = Column(String(255),nullable = False)
    corporate_or_registration_name = Column(String(32),nullable = True)
    website                        = Column(String(100),nullable = False)
    shop_category                  = Column(String,nullable = False) #groceries
    business_structure             = Column(String(255),nullable = False)#company
    in_charge                      = Column(String(255),nullable = True)# owner
    business_phone_number          =Column(String(20), nullable=False, unique=True)
    address1                       = Column(String(255), nullable=True)
    address2                       = Column(String(255), nullable=True)
    postal_code                    = Column(String(20), nullable=False)
    city                           = Column(String(255), nullable=False)   
    district                       = Column(String(255), nullable=False)
    state                          =  Column(String(255), nullable=False)
    local_bodies                   = Column(String(20), nullable=True)
    upload_shop_photo              =Column(String(200), nullable=True)

class Merchant_kyc_update(Base):

    __tablename__ = "merchant_kyc_update"
    id            = Column(Integer, primary_key=True)
    merchant_id   = Column(Integer, ForeignKey("merchant_profile_info.id"), unique = True, nullable = False)
    pan_number    = Column(String(20), nullable=True)
    name_on_pan   = Column(String(50), nullable=True)
    upload_pan    = Column(String(1024), nullable=True)
    gstin_number  = Column(String(20), nullable=True)
    tan_number    = Column(String(20), nullable=True)
    gst_number    = Column(String(20), nullable=True)
    kyc_doc_type  = Column(String(50), nullable=True)
    kyc_doc_front = Column(String(1024), nullable=True)
    kyc_doc_back  = Column(String(1024), nullable=True)



