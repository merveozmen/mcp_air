# mock_data.py

FLIGHT_DATA = {
    ("IST", "2026-01-20"): [
        {
            "flight_no": "TK101",
            "direction": "departure",
            "aircraft": "A321",
            "capacity": 180,
            "avg_load_factor": 0.85
        },
        {
            "flight_no": "TK202",
            "direction": "arrival",
            "aircraft": "B737",
            "capacity": 160,
            "avg_load_factor": 0.78
        },
        {
            "flight_no": "TK303",
            "direction": "departure",
            "aircraft": "A330",
            "capacity": 250,
            "avg_load_factor": 0.90
        }
    ],
    ("IST", "2026-01-21"): [
        {
            "flight_no": "TK404",
            "direction": "arrival",
            "aircraft": "A320",
            "capacity": 170,
            "avg_load_factor": 0.80
        },
        {
            "flight_no": "TK505",
            "direction": "departure",
            "aircraft": "B787",
            "capacity": 290,
            "avg_load_factor": 0.88
        }
    ]
}
