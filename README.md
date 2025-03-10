# status-page
Este es un simple monitor de servicios que verifica el estado de diferentes tipos de servicios (HTTP/S, SAMP, etc.) y muestra su estado en una interfaz web.

## Requisitos

- Python 3.x
- Librerías necesarias: `flask`, `requests`, `urllib3`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias necesarias:

   ```bash
   pip install flask requests urllib3
   ```

3. Asegúrate de tener los archivos `config.json` y `services.json` en el mismo directorio que el script.

## Configuración

### `config.json`

Este archivo contiene la configuración básica de la aplicación, como el host y el puerto en el que se ejecutará el servidor Flask.

Ejemplo de `config.json`:

```json
{
    "host": "0.0.0.0",
    "port": 5000,
    "debug": true
}
```

### `services.json`

Este archivo contiene la lista de servicios que se van a monitorear. Cada servicio debe tener un nombre, un tipo (HTTP/S, SAMP, etc.) y un destino (URL o dirección IP con puerto).

Ejemplo de `services.json`:

```json
[
    {
        "name": "My Website",
        "type": "HTTP/S",
        "destination": "https://example.com"
    },
    {
        "name": "My SAMP Server",
        "type": "SAMP",
        "destination": "127.0.0.1:7777"
    }
]
```

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el script de Python:

```bash
python app.py
```

La aplicación estará disponible en `http://<host>:<port>`, donde `<host>` y `<port>` son los valores configurados en `config.json`.


![image](https://github.com/user-attachments/assets/032c2ace-e79f-4603-819d-643a41418b7e)

