from pydantic import BaseModel
import hashlib


class RolesBase(BaseModel):
    description: str


class RolesCreate(RolesBase):
    pass


class Roles(RolesBase):
    id: int

    class Config:
        orm_mode = True


class ClaimsBase(BaseModel):
    description: str
    active: bool


class ClaimsCreate(ClaimsBase):
    pass


class Claim(ClaimsBase):
    id: int

    class Config:
        orm_mode = True


class UsersBase(BaseModel):
    name: str
    email: str
    role_id: int


class UsersCreate(UsersBase):
    password: str


class Users(UsersBase):
    id: int

    class Config:
        orm_mode = True


class UserClaimsBase(BaseModel):
    pass


class UserClaimsCreate(UserClaimsBase):
    pass


class UserClaims(UserClaimsBase):
    user_id: int
    claim_id: int

    class Config:
        orm_mode = True
