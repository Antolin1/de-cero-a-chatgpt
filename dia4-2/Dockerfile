FROM python:3.11-slim


WORKDIR /app
COPY calculator_mcp.py /app/calculator_mcp.py
RUN pip install --no-cache-dir "mcp[cli]"

# Stdio MCP server
CMD ["python", "/app/calculator_mcp.py"]