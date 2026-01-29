from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Server")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Fetch the current weather for a given location."""
    # In a real implementation, you would fetch data from a weather API.
    # Here, we return a mock response.
    return f"The current weather in {location} is Sunny, 25°C."

if __name__ == "__main__":
    print("Hello from weather_server!")
    mcp.run(transport="sse")