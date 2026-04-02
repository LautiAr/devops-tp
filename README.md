# DevOps TP Integrador

## Descripcion
API hecha con Flask para generar contraseñas aleatoras con letras, numeros y caracteres especiales.

---

## Endpoints

### Generar contraseña

GET /len/longitud

longitud = es un **int** que indica la longitud de la contraseña a generarse

#### Ejemplo:

/len/10

```json

{
  "password": "WwnL2!dzVG"
}

```

### Health

GET /health

Permite corroborar el estado de la API

#### Respuesta:

```json

{
  "status": "ok"
}

```

---

## Docker Setup

La aplicacion ahora puede correr en docker.

### Build Docker Image:

```bash
sudo docker build -t <nombre> .

sudo docker run -p 5000:5000 <nombre>
```

Para acceder: **127.0.0.1:5000/len/longitud**
