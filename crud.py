from sqlalchemy.orm import Session
import models
import schemas
import hashlib


def create_role(db: Session, role: schemas.RolesCreate):
    db_role = models.Roles(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def create_claim(db: Session, claim: schemas.ClaimsCreate):
    db_claim = models.Claims(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim


def create_user(db: Session, user: schemas.UsersCreate):
    encoded = user.password.encode()
    senha_encypt = hashlib.sha256(encoded).hexdigest()
    db_user = models.Users(
        name=user.name, email=user.email,
        password=senha_encypt, role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_userclaim(db: Session, user_claim: schemas.UserClaimsCreate):
    db_user_claim = models.UserClaims(**user_claim.dict())
    db.add(db_user_claim)
    db.commit()
    db.refresh(db_user_claim)
    return db_user_claim


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.Users).filter(models.Users.email == user_email).first()
