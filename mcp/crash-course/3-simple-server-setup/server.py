from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
from typing import Literal

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Run the server
if __name__ == "__main__":
    transport_env = os.getenv("TRANSPORT", "stdio")
    trs: Literal["stdio", "sse"]
    if transport_env == "sse":
        trs = "sse"
    else:
        trs = "stdio"
    mcp.run(trs)
