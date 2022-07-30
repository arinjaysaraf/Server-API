from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        schema_extra ={
            "post_demo": {
                "title":"Some title about animals",
                "content":"Some content about animals"
            }
        } 

# General user Schema to handle registration
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "name" : "Ram",
                "email" : "ram123@gmail.com",
                "password":"Ramkumar@123"
            }
        }

# schema for login
class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "email" : "ram123@gmail.com",
                "password":"Ramkumar@123"
            }
        }