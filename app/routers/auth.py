from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import oauth2
from ..database import get_db
from ..  import schemas, models, utils
from ..schemas import Token


router = APIRouter(tags=["authentication"])

@router.post("/login", response_model=Token)
def login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()],db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if  not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return Token(access_token=access_token, token_type="bearer")