import random
from sqlalchemy.orm import Session
from twilio.rest import Client

from .schema import merchant_details
from .models import MerchantInfo, MerchantBusinessInfo,Merchant_kyc_update




def check_if_merchant_email_exist(db: Session, email :str):
    return db.query(MerchantInfo).filter(MerchantInfo.email==email).first()

  
def check_if_gstin_number_exist(db:Session, gstin_number: str):
    return db.query(MerchantBusinessInfo).filter(MerchantBusinessInfo.gstin_number==gstin_number).first()

def check_if_website_exist(db:Session, website:str):
    return db.query(MerchantBusinessInfo).filter(MerchantBusinessInfo.website == website).first()


def check_if_gst_exist(db : Session, gst_number: str):
    return db.query(Merchant_kyc_update).filter(Merchant_kyc_update.gst_number == gst_number).first()

def check_if_tan_exist(db: Session, tan_number:str):
    return db.query(Merchant_kyc_update).filter(Merchant_kyc_update.tan_number == tan_number).first()


def create_merchant_profile(db:Session, merchant:merchant_details):
    db_merchant_profile = MerchantInfo(
        merchant_name = merchant.merchant_name,
        authorized_person = merchant.authorized_person,
        contact_number =merchant.contact_number,
        email = merchant.email,
        dob = merchant.dob,       
        gender = merchant.gender,
        merchant_upi_id = merchant.merchant_upi_id, 
        percentage_of_commission_offered = merchant.percentage_of_commission_offered
    )
    db.add(db_merchant_profile)
    db.flush()
    merchant_profile_id = db_merchant_profile.id
    db_merchant_business = MerchantBusinessInfo(
        merchant_id =merchant_profile_id,
        gstin_number = merchant.gstin_number,
        registered_shop_name = merchant.registered_shop_name,
        corporate_or_registration_name = merchant.corporate_or_registration_name,
        website = merchant.website,
        shop_category = merchant.shop_category,
        business_structure = merchant.business_structure,
        in_charge = merchant.in_charge,
        business_phone_number = merchant.business_phone_number,
        address1 = merchant.address1,
        address2 = merchant.address2,
        postal_code = merchant.postal_code,
        city  = merchant.city,
        district = merchant.district,
        state = merchant.state,
        local_bodies = merchant.local_bodies
    )
    db.add(db_merchant_business)
    db.flush()
    db_merchant_kyc = Merchant_kyc_update(
        merchant_id = merchant_profile_id,
        pan_number =merchant.pan_number,
        name_on_pan = merchant.name_on_pan,
        gstin_number = merchant.gstin_number,
        tan_number = merchant.tan_number,
        gst_number = merchant.gst_number,
        kyc_doc_type =merchant.kyc_doc_type
    )
    
    db.add(db_merchant_kyc)
    db.flush()
    db.commit()
    db.refresh(db_merchant_profile)
    db.refresh(db_merchant_business)
    db.refresh(db_merchant_kyc)
    return db_merchant_profile, db_merchant_business, db_merchant_kyc


# def send_otp(registered_number:str):

#     account_sid = "AC51ab6df7120c668c91f21094392cd61f"
#     auth_token = "46cccf61a66e88b19a3aa79f0a18a9e5"
#     twilio_number = "+13156934217"
#     recipient_number = registered_number
    
#     otp = str(random.randint(100000, 999999))


#     client = Client(account_sid, auth_token)

#     message=client.messages.create(
#                 body="Your OTP is: " + otp,
#                 from_=twilio_number,
#                 to=recipient_number)
#     return  otp

# def verify_both_otp(received_otp: str):
#     get_otp = send_otp()
#     if get_otp == received_otp :
#         return True
#     else:
#         return False