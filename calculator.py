# calculator.py

def calculate_daily_passengers(flights: list) -> dict:
    total = 0
    arrivals = 0
    departures = 0

    for flight in flights:
        passengers = flight["capacity"] * flight["avg_load_factor"]
        total += passengers

        if flight["direction"] == "arrival":
            arrivals += passengers
        else:
            departures += passengers

    return {
        "total": int(total),
        "arrivals": int(arrivals),
        "departures": int(departures)
    }
