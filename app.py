# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

# ---------------------
# FastAPI instance
# ---------------------
app = FastAPI(title="Airport MCP Server")

# ---------- CORS Middleware ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # test / orchestrate domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- MCP MODELS ----------
class MCPInitializeRequest(BaseModel):
    client_name: str | None = None

class MCPToolCallRequest(BaseModel):
    name: str
    arguments: Dict[str, Any]

# ---------------------
# MCP ENDPOINTS
# ---------------------

@app.post("/mcp/initialize")
def mcp_initialize(payload: MCPInitializeRequest):
    return {
        "protocol_version": "1.0",
        "server_name": "airport-mcp",
        "capabilities": {
            "tools": True
        }
    }

@app.post("/mcp/tools/list")
def mcp_tools_list():
    return {
        "tools": [
            {
                "name": "get_daily_airport_usage",
                "title": "Daily Airport Usage Estimation",
                "description": "Returns estimated daily airport passenger usage",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "airport_code": {"type": "string", "title": "Airport Code"},
                        "date": {"type": "string", "title": "Date (YYYY-MM-DD)"}
                    },
                    "required": ["airport_code", "date"]
                }
            }
        ]
    }

@app.post("/mcp/tools/call")
def mcp_tools_call(payload: MCPToolCallRequest):
    if payload.name != "get_daily_airport_usage":
        return {"error": f"Unknown tool: {payload.name}"}

    airport_code = payload.arguments.get("airport_code")
    date = payload.arguments.get("date")

    if not airport_code or not date:
        raise HTTPException(
            status_code=400,
            detail="airport_code and date are required"
        )

    # ---------------------
    # Örnek hesaplama (sonradan gerçek logic ekleyebilirsin)
    # ---------------------
    estimated_passengers = 5000  # örnek sabit değer

    return {
        "content": [
            {
                "type": "text",
                "text": (
                    f"{airport_code} airport on {date} "
                    f"is expected to serve approximately {estimated_passengers} passengers."
                )
            }
        ]
    }

# ---------- Optional ping test ----------
@app.get("/ping", tags=["debug"])
def ping():
    return {"ping": "pong"}
