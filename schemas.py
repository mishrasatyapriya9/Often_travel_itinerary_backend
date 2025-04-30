# File: schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class ActivityCreate(BaseModel):
    name: str
    description: Optional[str] = None
    location: str
    day: int
    duration_hours: Optional[float] = None
    
    
class ActivityResponse(ActivityCreate):
    id: int
    
    class Config:
        orm_mode = True


class TransferCreate(BaseModel):
    day: int
    from_location: str
    to_location: str
    transfer_type: str
    
    
class TransferResponse(TransferCreate):
    id: int
    
    class Config:
        orm_mode = True


class AccommodationCreate(BaseModel):
    hotel_name: str
    room_type: Optional[str] = None
    location: str
    check_in_day: int
    num_nights: int
    
    
class AccommodationResponse(AccommodationCreate):
    id: int
    
    class Config:
        orm_mode = True


class ItineraryCreate(BaseModel):
    title: str
    description: Optional[str] = None
    region: str
    nights: int
    price: Optional[float] = None
    accommodations: List[AccommodationCreate]
    transfers: List[TransferCreate]
    activities: List[ActivityCreate]
    
    
class ItineraryResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    region: str
    nights: int
    price: Optional[float] = None
    created_at: date
    accommodations: List[AccommodationResponse]
    transfers: List[TransferResponse]
    activities: List[ActivityResponse]
    
    class Config:
        orm_mode = True


class ItineraryRecommendationResponse(BaseModel):
    id: int
    title: str
    region: str
    description: Optional[str] = None
    nights: int
    price: Optional[float] = None
    
    class Config:
        orm_mode = True
