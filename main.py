import fastapi
import uvicorn
from fastapi import Body, FastAPI, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "Elephant",
        "content": "Elephant is a large, two-toed ungulate mammal in the family Elephantidae."
    },
    {
        "id": 2,
        "title": "Lion",
        "content": "Lion is a large, solitary cat in the family Felidae."
    },
    {
        "id": 3,
        "title": "Crocodile",
        "content": "Crocodile is a large, carnivorous, predatory fish in the family Crocodylidae."
    }
]

users = []  # appended later


app = FastAPI()

# Get - for testing
@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}

# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data":posts}


# Get Post by ID
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if (id>len(posts)):
        return {
            "message":"Post not found"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data":post
            }

#Posts a single post{A handler for the POST request}
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"Post Added!"
    }

# for user SignUp {New User}
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

# if a user already exists before creating a JWT with the user mail
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

# for user login
@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"INVALID Login Credentials!"
        }