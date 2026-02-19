from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My calculator MCP server 😃")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float|str:
    """Divide two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b

@mcp.prompt()
def query_prompt() -> str:
    """Guidelines on how to use my calculator MCP server."""
    return """Whenenver the request is related to basic arithmetic operations, use the MCP server tools, please 🌞"""


if __name__ == "__main__":
    mcp.run()