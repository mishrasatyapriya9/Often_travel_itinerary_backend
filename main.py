# File: main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
from database import engine, get_db

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Itinerary API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/itineraries/", response_model=schemas.ItineraryResponse, status_code=status.HTTP_201_CREATED)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    """Create a new trip itinerary."""
    db_itinerary = models.Itinerary(
        title=itinerary.title,
        description=itinerary.description,
        region=itinerary.region,
        nights=itinerary.nights,
        price=itinerary.price
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    
    # Add accommodations
    for acc in itinerary.accommodations:
        db_acc = models.Accommodation(
            itinerary_id=db_itinerary.id,
            hotel_name=acc.hotel_name,
            room_type=acc.room_type,
            location=acc.location,
            check_in_day=acc.check_in_day,
            num_nights=acc.num_nights
        )
        db.add(db_acc)
    
    # Add transfers
    for transfer in itinerary.transfers:
        db_transfer = models.Transfer(
            itinerary_id=db_itinerary.id,
            day=transfer.day,
            from_location=transfer.from_location,
            to_location=transfer.to_location,
            transfer_type=transfer.transfer_type
        )
        db.add(db_transfer)
    
    # Add activities
    for activity in itinerary.activities:
        db_activity = models.Activity(
            itinerary_id=db_itinerary.id,
            name=activity.name,
            description=activity.description,
            location=activity.location,
            day=activity.day,
            duration_hours=activity.duration_hours
        )
        db.add(db_activity)
    
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

@app.get("/itineraries/", response_model=List[schemas.ItineraryResponse])
def get_itineraries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all trip itineraries."""
    return db.query(models.Itinerary).offset(skip).limit(limit).all()

@app.get("/itineraries/{itinerary_id}", response_model=schemas.ItineraryResponse)
def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """Get a specific trip itinerary by ID."""
    db_itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()
    if db_itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return db_itinerary