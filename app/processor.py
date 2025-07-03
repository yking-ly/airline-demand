from collections import Counter
from app.amadeus_client import get_airline_name

def get_popular_routes(data):
    routes = []
    for offer in data:
        segments = offer["itineraries"][0]["segments"]
        route = f"{segments[0]['departure']['iataCode']} → {segments[-1]['arrival']['iataCode']}"
        routes.append(route)
    most_common = Counter(routes).most_common(5)
    return most_common

def summarize_offers(data):
    offers = []
    for offer in data:
        price = offer["price"]["total"]
        segments = offer["itineraries"][0]["segments"]
        route = f"{segments[0]['departure']['iataCode']} → {segments[-1]['arrival']['iataCode']}"
        stops = len(segments) - 1
        duration = offer["itineraries"][0]["duration"]
        airline = segments[0]["carrierCode"]
        airline_code = segments[0]["carrierCode"]
        airline_name = get_airline_name(airline_code)


        offers.append({
            "route": route,
            "price": float(price),
            "stops": stops,
            "duration": offer["itineraries"][0]["duration"],
            "airline": airline_name
        })
    return offers

