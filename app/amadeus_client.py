from amadeus import Client, ResponseError
import os
from dotenv import load_dotenv

load_dotenv()

amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET")
)

def fetch_flight_offers(origin: str, destination: str, date: str):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=1,
            max=10
        )
        return response.data
    except ResponseError as error:
        print(error)
        return []

def get_airline_name(iata_code: str) -> str:
    try:
        response = amadeus.reference_data.airlines.get(airlineCodes=iata_code)
        if response.data and "businessName" in response.data[0]:
            return response.data[0]["businessName"]
        elif response.data and "commonName" in response.data[0]:
            return response.data[0]["commonName"]
        else:
            return iata_code  # fallback to code
    except Exception:
        return iata_code
