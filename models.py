# File: models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Itinerary(Base):
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    region = Column(String(50), nullable=False)
    nights = Column(Integer, nullable=False)
    price = Column(Float)
    created_at = Column(Date, default=datetime.now)
    
    # Relationships
    accommodations = relationship("Accommodation", back_populates="itinerary", cascade="all, delete-orphan")
    transfers = relationship("Transfer", back_populates="itinerary", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="itinerary", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "region": self.region,
            "nights": self.nights,
            "price": self.price,
            "created_at": str(self.created_at),
            "accommodations": [acc.to_dict() for acc in self.accommodations],
            "transfers": [transfer.to_dict() for transfer in self.transfers],
            "activities": [activity.to_dict() for activity in self.activities]
        }


class Accommodation(Base):
    __tablename__ = "accommodations"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)
    hotel_name = Column(String(100), nullable=False)
    room_type = Column(String(50))
    location = Column(String(100), nullable=False)
    check_in_day = Column(Integer, nullable=False)  # Day 1, Day 2, etc.
    num_nights = Column(Integer, nullable=False)
    
    # Relationships
    itinerary = relationship("Itinerary", back_populates="accommodations")
    
    def to_dict(self):
        return {
            "id": self.id,
            "hotel_name": self.hotel_name,
            "room_type": self.room_type,
            "location": self.location,
            "check_in_day": self.check_in_day,
            "num_nights": self.num_nights
        }


class Transfer(Base):
    __tablename__ = "transfers"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)
    day = Column(Integer, nullable=False)
    from_location = Column(String(100), nullable=False)
    to_location = Column(String(100), nullable=False)
    transfer_type = Column(String(50), nullable=False)  # Ferry, Car, etc.
    
    # Relationships
    itinerary = relationship("Itinerary", back_populates="transfers")
    
    def to_dict(self):
        return {
            "id": self.id,
            "day": self.day,
            "from_location": self.from_location,
            "to_location": self.to_location,
            "transfer_type": self.transfer_type
        }


class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    location = Column(String(100), nullable=False)
    day = Column(Integer, nullable=False)
    duration_hours = Column(Float)
    
    # Relationships
    itinerary = relationship("Itinerary", back_populates="activities")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "day": self.day,
            "duration_hours": self.duration_hours
        }
