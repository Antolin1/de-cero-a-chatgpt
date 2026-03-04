# Instrucciones para ejecutar y registrar el MCP server

1. Construir la imagen Docker:

   ```bash
   docker build -t calculator_mcp .
   ```
2. Registrar el servidor MCP en alguna aplicación IA. Por ejemplo, en el GitHub Copilot de VSCode, añadir la siguiente configuración:

   ```json
   "my_calculator_mcp": {
       "type": "stdio",
       "command": "docker",
       "args": [
         "run",
         "-i",
         "--rm",
         "calculator_mcp"
       ]
   }
   ```
   Esto se hace con Control + Shift + P -> "GitHub Copilot: Add MCP server" -> Command stdio --> `docker run -i --rm calculator_mcp`.

# Ejercicio MCP I

Crea una servidor MCP que se conecte a la base de datos `Chinook_Sqlite.sqlite` y responda preguntas en lenguaje natural. Conéctalo con GitHub Copilot del VS Code.

**Pistas**: El Dockerfile debe instalar las liberías necesarias y copiar la base de datos al contenedor (junto con el script que implementa el servidor MCP).

# Ejercicio MCP II

Investiga como conectar el servidor MCP a un agente smolagent y LangChain. En otras palabras, instancia un agente usando esas librerías cuyas herramientas sean las expuestas por tu servidor MCP.

Links útiles:
- https://docs.langchain.com/oss/python/langchain/mcp
- https://huggingface.co/docs/smolagents/tutorials/tools#use-tools-from-an-mcp-server