from models import User
from fastapi import FastAPI, HTTPException
from jose import jwt
from utils import conn,cur

app = FastAPI()
payload  = {"user_id": 1,  "role": "user"}
secret_key = "mysecret"
token = jwt.encode(payload, secret_key, algorithm="HS256")
@app.post("/route")
def protected_route(token: str):
data = jwt.decode(token, secret_key, algorithms=["HS256"])
print(data)
return {"status": "success", "user_data": token}
@app.post("/register")
def register(user: User):
if not user.name or not user.age:
raise HTTPException(status_code=404, detail="user not found")
cur.execute("INSERT INTO users VALUES(%s,%s)", (user.name, user.age))
conn.commit()
return {"status": "success", "user_name":user.name, "user_age": user.age}
@app.get("/users/{user_id}")
def getting(user_id: int):
cur.execute("SELECT*FROM users")
users  = cur.fetchall()
cur.close()
conn.close()
return {"status": "success", "user": [{"name": user[0], "age": user[1]} for user in users] }
