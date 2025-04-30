# File: mcp_server.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
from database import get_db

app = FastAPI()

mcp_app = FastAPI(title="MCP Recommendation Server")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mcp_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@mcp_app.get("/recommendations/{nights}", response_model=List[schemas.ItineraryRecommendationResponse])
def get_recommendations(nights: int, db: Session = Depends(get_db)):
    """Get recommended itineraries for a given number of nights."""
    recommended_itineraries = db.query(models.Itinerary).filter(models.Itinerary.nights == nights).all()
    
    if not recommended_itineraries:
        raise HTTPException(status_code=404, detail=f"No recommended itineraries found for {nights} nights")
    
    return recommended_itineraries