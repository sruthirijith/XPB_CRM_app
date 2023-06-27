
from pydantic import BaseModel, EmailStr



class login(BaseModel):

    Email    : EmailStr
    Password : str

 


        
        