# app/controllers/auth.py

from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .token import create_access_token
from ..classes.user import User, Role
from ..database import SessionLocal

from sqlalchemy.orm import Session

from typing import Optional

from jose import JWTError, jwt
from datetime import datetime, timedelta

# Define a function to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = get_user(db, token_data.username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# Define a function to get the current user's role
def get_current_user_role(current_user: User = Depends(get_current_user)):
    return current_user.role

# Create an OAuth2PasswordBearer instance for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define a function to verify the user's password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Define a function to get a user by username
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Define a function to authenticate a user and create a token
def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# Define a function to create an access token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Define a function to create a new user (registration)
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, role=user.role, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Define a function to get the current user's role
def get_current_user_role(current_user: User = Depends(get_current_user)):
    return current_user.role

# Define a function to check if a user has the required role (authorization)
def check_user_role(required_role: Role, current_user_role: Role = Depends(get_current_user_role)):
    if current_user_role != required_role and current_user_role != Role.director:
        raise HTTPException(status_code=403, detail="Permission denied")
