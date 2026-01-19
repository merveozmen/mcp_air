from fastapi import FastAPI, HTTPException
from mock_data import FLIGHT_DATA
from calculator import calculate_daily_passengers
import os

app = FastAPI(
    title="Airport Usage MCP Server",
    description="Daily airport passenger estimation",
    version="1.0.0"
)

@app.post("/get_daily_airport_usage")
def get_daily_airport_usage(payload: dict):
    airport_code = payload.get("airport_code")
    date = payload.get("date")

    if not airport_code or not date:
        raise HTTPException(
            status_code=400,
            detail="airport_code and date are required"
        )

    key = (airport_code, date)
    flights = FLIGHT_DATA.get(key)

    if not flights:
        return {
            "airport_code": airport_code,
            "date": date,
            "estimated_passengers": 0,
            "confidence": 0.3,
            "message": "No flight data available"
        }

    stats = calculate_daily_passengers(flights)

    return {
        "airport_code": airport_code,
        "date": date,
        "estimated_passengers": stats["total"],
        "confidence": 0.85,
        "breakdown": {
            "arrivals": stats["arrivals"],
            "departures": stats["departures"],
            "flight_count": len(flights)
        }
    }
