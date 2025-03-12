from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    workouts = relationship("Workout", back_populates="user", cascade="all, delete")

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    exercise = Column(String, nullable=False)
    category = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="workouts")
