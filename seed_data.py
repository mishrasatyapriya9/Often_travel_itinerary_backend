# File: seed_data.py
from database import SessionLocal, engine
import models
from datetime import datetime

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    # Clear existing data
    db.query(models.Activity).delete()
    db.query(models.Transfer).delete()
    db.query(models.Accommodation).delete()
    db.query(models.Itinerary).delete()
    
    # Create sample data for Phuket 3-night itinerary
    phuket_3night = models.Itinerary(
        title="Phuket Beach Relaxation",
        description="Experience the best beaches and relaxing atmosphere of Phuket in 3 nights",
        region="Phuket",
        nights=3,
        price=299.99,
        created_at=datetime.now()
    )
    db.add(phuket_3night)
    db.commit()
    db.refresh(phuket_3night)
    
    # Add accommodations
    phuket_hotel = models.Accommodation(
        itinerary_id=phuket_3night.id,
        hotel_name="Patong Beach Resort",
        room_type="Deluxe Sea View",
        location="Patong Beach, Phuket",
        check_in_day=1,
        num_nights=3
    )
    db.add(phuket_hotel)
    
    # Add transfers
    airport_transfer = models.Transfer(
        itinerary_id=phuket_3night.id,
        day=1,
        from_location="Phuket International Airport",
        to_location="Patong Beach Resort",
        transfer_type="Private Car"
    )
    db.add(airport_transfer)
    
    departure_transfer = models.Transfer(
        itinerary_id=phuket_3night.id,
        day=4,
        from_location="Patong Beach Resort",
        to_location="Phuket International Airport",
        transfer_type="Private Car"
    )
    db.add(departure_transfer)
    
    # Add activities
    beach_day = models.Activity(
        itinerary_id=phuket_3night.id,
        name="Patong Beach Day",
        description="Enjoy a full day at the famous Patong Beach",
        location="Patong Beach",
        day=1,
        duration_hours=5.0
    )
    db.add(beach_day)
    
    phi_phi = models.Activity(
        itinerary_id=phuket_3night.id,
        name="Phi Phi Islands Tour",
        description="Full day speedboat tour to the beautiful Phi Phi Islands",
        location="Phi Phi Islands",
        day=2,
        duration_hours=8.0
    )
    db.add(phi_phi)
    
    old_town = models.Activity(
        itinerary_id=phuket_3night.id,
        name="Phuket Old Town Walking Tour",
        description="Explore the charming streets and history of Phuket Old Town",
        location="Phuket Old Town",
        day=3,
        duration_hours=3.0
    )
    db.add(old_town)
    
    # Create Krabi 2-night itinerary
    krabi_2night = models.Itinerary(
        title="Krabi Adventure Escape",
        description="Short but sweet adventure in the stunning landscapes of Krabi",
        region="Krabi",
        nights=2,
        price=199.99,
        created_at=datetime.now()
    )
    db.add(krabi_2night)
    db.commit()
    db.refresh(krabi_2night)
    
    # Add accommodations
    krabi_hotel = models.Accommodation(
        itinerary_id=krabi_2night.id,
        hotel_name="Ao Nang Cliff Beach Resort",
        room_type="Superior Room",
        location="Ao Nang, Krabi",
        check_in_day=1,
        num_nights=2
    )
    db.add(krabi_hotel)
    
    # Add transfers
    krabi_arrival = models.Transfer(
        itinerary_id=krabi_2night.id,
        day=1,
        from_location="Krabi Airport",
        to_location="Ao Nang Cliff Beach Resort",
        transfer_type="Shared Minivan"
    )
    db.add(krabi_arrival)
    
    krabi_departure = models.Transfer(
        itinerary_id=krabi_2night.id,
        day=3,
        from_location="Ao Nang Cliff Beach Resort",
        to_location="Krabi Airport",
        transfer_type="Shared Minivan"
    )
    db.add(krabi_departure)
    
    # Add activities
    four_islands = models.Activity(
        itinerary_id=krabi_2night.id,
        name="Four Islands Tour",
        description="Visit the stunning islands of Koh Poda, Chicken Island, Tup Island and Phra Nang Cave Beach",
        location="Krabi Islands",
        day=1,
        duration_hours=7.0
    )
    db.add(four_islands)
    
    hot_springs = models.Activity(
        itinerary_id=krabi_2night.id,
        name="Emerald Pool and Hot Springs",
        description="Visit the natural Emerald Pool and relax in the hot springs",
        location="Khlong Thom, Krabi",
        day=2,
        duration_hours=6.0
    )
    db.add(hot_springs)
    
    # Create Phuket-Krabi 5-night itinerary
    combo_5night = models.Itinerary(
        title="Phuket & Krabi Highlights",
        description="Experience the best of both Phuket and Krabi in this 5-night combo",
        region="Phuket & Krabi",
        nights=5,
        price=499.99,
        created_at=datetime.now()
    )
    db.add(combo_5night)
    db.commit()
    db.refresh(combo_5night)
    
    # Add accommodations
    phuket_combo_hotel = models.Accommodation(
        itinerary_id=combo_5night.id,
        hotel_name="Phuket Marriott Resort",
        room_type="Garden View Room",
        location="Merlin Beach, Phuket",
        check_in_day=1,
        num_nights=3
    )
    db.add(phuket_combo_hotel)
    
    krabi_combo_hotel = models.Accommodation(
        itinerary_id=combo_5night.id,
        hotel_name="Railay Princess Resort",
        room_type="Deluxe Room",
        location="Railay Beach, Krabi",
        check_in_day=4,
        num_nights=2
    )
    db.add(krabi_combo_hotel)
    
    # Add transfers
    arrival_transfer = models.Transfer(
        itinerary_id=combo_5night.id,
        day=1,
        from_location="Phuket International Airport",
        to_location="Phuket Marriott Resort",
        transfer_type="Private Car"
    )
    db.add(arrival_transfer)
    
    phuket_to_krabi = models.Transfer(
        itinerary_id=combo_5night.id,
        day=4,
        from_location="Phuket Marriott Resort",
        to_location="Railay Princess Resort",
        transfer_type="Ferry + Longtail Boat"
    )
    db.add(phuket_to_krabi)
    
    final_departure = models.Transfer(
        itinerary_id=combo_5night.id,
        day=6,
        from_location="Railay Princess Resort",
        to_location="Krabi Airport",
        transfer_type="Longtail Boat + Private Car"
    )
    db.add(final_departure)
    
    # Add activities for the combo tour
    phi_phi_tour = models.Activity(
        itinerary_id=combo_5night.id,
        name="Phi Phi Islands Tour",
        description="Full day speedboat tour to the beautiful Phi Phi Islands",
        location="Phi Phi Islands",
        day=2,
        duration_hours=8.0
    )
    db.add(phi_phi_tour)
    
    phang_nga = models.Activity(
        itinerary_id=combo_5night.id,
        name="Phang Nga Bay Tour",
        description="Explore the limestone karsts of Phang Nga Bay and visit James Bond Island",
        location="Phang Nga Bay",
        day=3,
        duration_hours=7.0
    )
    db.add(phang_nga)
    
    rock_climbing = models.Activity(
        itinerary_id=combo_5night.id,
        name="Rock Climbing at Railay",
        description="Rock climbing adventure on the limestone cliffs of Railay",
        location="Railay Beach",
        day=4,
        duration_hours=4.0
    )
    db.add(rock_climbing)
    
    hong_island = models.Activity(
        itinerary_id=combo_5night.id,
        name="Hong Island Tour",
        description="Visit the stunning Hong Island and lagoon",
        location="Hong Island",
        day=5,
        duration_hours=6.0
    )
    db.add(hong_island)
    
    # Create more sample itineraries for different durations
    phuket_4night = models.Itinerary(
        title="Phuket Family Adventure",
        description="Family-friendly 4-night adventure in Phuket",
        region="Phuket",
        nights=4,
        price=399.99,
        created_at=datetime.now()
    )
    db.add(phuket_4night)
    db.commit()
    
    krabi_7night = models.Itinerary(
        title="Krabi Ultimate Relaxation",
        description="Extended 7-night stay in the beautiful Krabi province",
        region="Krabi",
        nights=7,
        price=699.99,
        created_at=datetime.now()
    )
    db.add(krabi_7night)
    db.commit()
    
    phuket_krabi_8night = models.Itinerary(
        title="Thailand South Ultimate Experience",
        description="Comprehensive 8-night tour of Phuket and Krabi",
        region="Phuket & Krabi",
        nights=8,
        price=899.99,
        created_at=datetime.now()
    )
    db.add(phuket_krabi_8night)
    db.commit()
    
    phuket_6night = models.Itinerary(
        title="Phuket Luxury Escape",
        description="Luxury 6-night escape to Phuket's best resorts",
        region="Phuket",
        nights=6,
        price=799.99,
        created_at=datetime.now()
    )
    db.add(phuket_6night)
    db.commit()
    
    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed_database()