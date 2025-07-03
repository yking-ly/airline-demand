from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from app.amadeus_client import fetch_flight_offers
from app.processor import summarize_offers, get_popular_routes
from app.database import init_db
from app.database import SessionLocal, FlightSearch
from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi import Query
from app.amadeus_client import amadeus

app = FastAPI()
init_db()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/suggest")
def airport_suggestions(q: str = Query(..., min_length=1)):
    try:
        response = amadeus.reference_data.locations.get(
            keyword=q,
            subType="AIRPORT",
            page={"limit": 5}
        )
        suggestions = [
            {
                "iataCode": loc["iataCode"],
                "name": loc["name"],
                "city": loc["address"]["cityName"]
            }
            for loc in response.data
        ]
        return JSONResponse(suggestions)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/search")
async def search(
    request: Request,
    origin: str = Form(...),
    destination: str = Form(...),
    date: str = Form(...)
):
    # Fetch raw data from Amadeus API
    raw_data = fetch_flight_offers(origin, destination, date)

    # Process and extract insights
    summary = summarize_offers(raw_data)
    popular = get_popular_routes(raw_data)

     # Store to DB
    db = SessionLocal()
    try:
        for offer in summary:
            db_record = FlightSearch(
                origin=origin,
                destination=destination,
                route=offer["route"],
                price=offer["price"],
                departure_date=datetime.strptime(date, "%Y-%m-%d").date(),
                stops=offer["stops"],
                duration=offer["duration"],
                airline=offer["airline"]
            )
            db.add(db_record)
        db.commit()
    finally:
        db.close()
    # Render the updated template with all data
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "origin": origin,
        "destination": destination,
        "date": date,
        "popular": popular
    })

@app.get("/dashboard")
def dashboard(request: Request):
    db = SessionLocal()
    try:
        # Group by destination + month and average price
        results = db.execute(text("""
        SELECT 
            origin,
            destination,
            strftime('%Y-%m', departure_date) as month,
            COUNT(*) as search_count,
            AVG(price) as avg_price
        FROM flight_searches
        GROUP BY origin, destination, month
        ORDER BY search_count DESC
        LIMIT 10
        """)).fetchall()
    finally:
        db.close()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "results": results
    })

