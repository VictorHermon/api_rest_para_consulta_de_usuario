from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from datetime import datetime


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


class Claims(Base):
    __tablename__ = 'claims'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_at = Column(DateTime, default=datetime.utcnow)


class UserClaims(Base):
    __tablename__ = 'user_claims'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    claim_id = Column(Integer, ForeignKey('claims.id'), unique=True, nullable=False)
