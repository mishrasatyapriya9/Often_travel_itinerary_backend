# 🌐 Travel Itinerary Management System - Backend

This repository contains the **FastAPI backend implementation** for the Thailand Travel Itinerary system. It powers the frontend with endpoints to manage travel plans, retrieve curated trips, and provide intelligent recommendations for destinations like **Phuket** and **Krabi**.

---

## ✨ Features

* **Full CRUD for Itineraries** – Create, read, update, and delete itineraries with detailed structure.
* **MCP (Most Common Preferences) Recommendation** – Suggests itineraries based on user preferences like duration and location.
* **Day-by-Day Breakdown** – Each itinerary supports detailed daily plans, hotels, transfers, and activities.
* **Pydantic Models** – Ensures request/response data validation.
* **Clean Modular Codebase** – Easily maintainable and scalable FastAPI structure.
* **CORS Configured** – Ready for seamless frontend-backend communication.

---

## 🧪 Tech Stack

* **Python 3.10+**
* **FastAPI** – Web framework
* **SQLAlchemy** – ORM for database modeling
* **SQLite** – Lightweight database (can be replaced with PostgreSQL)
* **Uvicorn** – ASGI server for running FastAPI
* **Pydantic** – Schema validation

---

---

## ⚙️ Setup Instructions

### *Prerequisites:*

* Python 3.10+
* `pip` installed
* (I am using this way) Use a virtual environment : `python -m venv venv`

---

## 🚀 Getting Started

Instructions on how to run Backend locally can be added here.

Environment Setup
### *1. Clone the repository:*

```bash
git clone https://github.com/mishrasatyapriya9/Often_travel_itinerary_backend
cd Often_travel_itinerary_backend
```

## 🚀 Backend Setup Commands (Windows)

Use the following commands to set up and run the backend and MCP recommendation server:

### 🛠️ Create and activate a virtual environment
# Install venv to the project
```bash
python -m venv venv               # Install venv to the project
```

# Activate the Python virtual environment (Windows)
```bash
venv\Scripts\activate             
```


---

### *2. Install dependencies:*

```bash
pip install -r requirements.txt
```

---

### *3. Run the development server:*

```bash
uvicorn app.main:app --reload
```

*The backend will start at:*  
```
http://127.0.0.1:8000
```
### *. Add More Terminal , Run the development server for MCP:*
## Start the MCP server to get itinerary recommendations
```bash
uvicorn mcp_server:mcp_app --port 8001 --reload   
```

*The backend will start at:*  
```
http://127.0.0.1:8001
```

---

## 📬 API Endpoints Overview

* GET / :  Retrieves all existing itineraries 
* GET /itineraries/{id}  : Fetches detailed information about a specific itinerary with each and every details 
* POST /create : Creates a new custom itinerary according to User 
* GET /recommendations  : Returns recommended itineraries based on 

---

## 🔐 Recommendation Logic (MCP)

* Accepts inputs like **trip duration** which is nights .
* Returns curated itineraries matching most common user behavior for those inputs.
* Useful for first-time travelers or quick planning.


## 🛠️ Future Enhancements

* Add authentication and user profiles
* Add Chatbot 
* Add unit and integration tests
* Integrate with Google Places or other travel APIs

---

## 🔗 Related Projects

* **Frontend Repository:**  
  [Often Travel Itinerary Frontend](https://github.com/mishrasatyapriya9/Often-travel-itinerary-frontend)

---

## 👨‍💻 Author

**Satyapriya Mishra** – Full Stack SDE Intern  
Built with ❤️ using FastAPI and React

---

                                           
