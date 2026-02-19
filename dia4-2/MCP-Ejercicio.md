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

   # Ejercicio MCP

   Crea una servidor MCP que se conecte a la base de datos `Chinook_Sqlite.sqlite` y responda preguntas en lenguaje natural. 

   **Pistas**: El dockerfile debe instalar las liberías necesarias y copiar la base de datos al contenedor (junto con el script que implementa el servidor MCP).