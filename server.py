
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("Simple Calculator Server")


# Tool 1: Add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return their sum."""
    return a + b


# Tool 2: Generate a greeting
@mcp.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting."""
    return f"Hello, {name}! Welcome to our MCP server."


# Tool 3: Calculate rectangle area
@mcp.tool()
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width


# Tool 4: Get server information
@mcp.tool()
def get_server_info() -> str:
    """Return basic information about this MCP server."""
    return (
        "Server Name: Simple Calculator Server\n"
        "Technology: Python\n"
        "Framework: FastMCP\n"
        "Available Tools: 4"
    )


# Start MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")
