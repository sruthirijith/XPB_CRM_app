import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

##############################

def test_login_invalid_email():
    data ={"email":"sruthisr121@gmail.com"}
    response = client.post("/email_login",json=data)
    assert response.status_code ==404
    assert response.json() == { 
                "detail" : {
                "status": "Error",
                    "status_code": 404,
                    "data": None,
                    "error": {
                        "status_code": 404,
                        "status": "Error",
                        "message": "Email not found!"
                    }
                }
                }
# def test_failed_login():    
#     data ={"email":"sruthisr21@gmail.com",
#            "password":"Sruthi@12345"}
    
#     response = client.post("/email_login", json=data)
#     assert response.status_code == 401
#     assert response.json() == { 
#                 "detail" : {
#                 "status": "Error",
#                         "status_code": 401,
#                         "data": None,
#                         "error": {
#                             "status_code": 401,
#                             "status": "Error",
#                             "message": "Login failed! Invalid credentials"
#                         }
#                     }
#                 }
# def test_succesful_login():
#     data ={"email":"sruthisr21@gmail.com",
#            "password":"Sruthi@1234"}
    
#     response = client.post("/email_login", json=data)
    # dict1 = response.json()['detail']
    # dict2 =(dict1.get('data'))
    # token = dict2.get('access_token')
    # refresh_token = dict2.get('refresh_token')
#     assert response.status_code == 200
#     assert response.json() == {             
#             "detail": {
#                 "status": "Success",
#                 "status_code": 200,
#                 "data": {
#                     "status_code": 200,
#                     "status": "Success",
#                     "message": "User Logged in Successfully",
#                     "id":1,
#                     "full_name": "Test Consumer",
#                     "email": "test@example.com",
#                     "phone_number": "+911234567891",
#                 },
#                 "error": None
#             }
#         }

# def test_forgot_password_invalid_email():
#     data =  {"email":"sruthisr211@gmail.com"}   
#     response = client.post("/forgot_password", json=data)
#     assert response.status_code ==404
#     assert response.json() == {
#                 "detail" : {
#                 "status": "Error",
#                 "status_code": 404,
#                 "data": None,
#                 "error": {
#                     "status_code": 404,
#                     "status": "Error",
#                     "message": "Email not found"
#                 }
#             }  
#         }
# def test_forgot_password_success(): 
#     data =  {"email":"sruthisr21@gmail.com"}   
#     response = client.post("/forgot_password", json=data) 
#     assert response.status_code ==201
#     assert response.json() == {
#                 "detail": {
#                     "status": "Success",
#                     "status_code": 200,
#                     "data": {
#                         "status_code": 200,
#                         "status": "Success",
#                         "message": "mail send successfully",
#                         "status": "Sucess",
#                         "email": "test@example.com",
                        

#                     },
#                     "error": None
#                 }
#             }  

