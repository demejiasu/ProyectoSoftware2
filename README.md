# Sistema de Microservicios - Ingeniería de Software II

## Autor

Estudiante: 1053863699

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema basado en **arquitectura de microservicios** que implementa funcionalidades básicas de un e-commerce, incluyendo gestión de usuarios, productos, órdenes y notificaciones. Todas las peticiones externas pasan obligatoriamente por un **API Gateway** centralizado, lo que garantiza un punto único de entrada y control sobre el tráfico hacia los diferentes servicios.

---

## Arquitectura del Sistema

El sistema está compuesto por **cinco microservicios independientes** que se comunican entre sí a través de APIs REST. A continuación se presenta el diagrama de la arquitectura general:

![Arquitectura del Sistema](diagrama.png)

### Tecnologías Utilizadas

| Componente | Tecnología | Framework | Base de Datos |
|------------|------------|-----------|---------------|
| **API Gateway** | Node.js | Express.js | - |
| **Auth Service** | PHP 8.4 | Laravel 12 | MySQL 8 |
| **User Service** | Python 3.10 | Django 5.2 | PostgreSQL 15 |
| **Product Service** | Python 3.10 | Flask 3.1 | MongoDB 6 |
| **Order Service** | Node.js 18 | Express.js | (en memoria) |
| **Notification Service** | Python 3.10 | Flask 3.1 | (en memoria) |
| **Frontend Web** | HTML/CSS/JS | - | - |

### Frameworks utilizados (obligatorios)
- ✅ **Laravel** (PHP) → Auth Service
- ✅ **Django** (Python) → User Service
- ✅ **Flask** (Python) → Product Service, Notification Service
- ✅ **Express** (Node.js) → API Gateway, Order Service

### Bases de datos utilizadas (obligatorias)
- ✅ **MySQL 8** → Auth Service
- ✅ **PostgreSQL 15** → User Service
- ✅ **MongoDB 6** → Product Service

---

## Frontend Web

El sistema incluye una **interfaz web completa** servida por el API Gateway en `http://localhost:3000`.

### Funcionalidades públicas (sin login)
| Sección | Descripción |
|---------|-------------|
| 🏠 **Inicio** | Hero con bienvenida y productos destacados |
| 📦 **Productos** | Catálogo completo con buscador y filtro por categorías |
| 🔐 **Iniciar Sesión** | Modal de login con "¿Olvidaste tu contraseña?" |
| 📝 **Registrarse** | Modal de registro de nuevos usuarios |

### Funcionalidades privadas (con login)

| Sección | Admin | Usuario normal |
|---------|-------|----------------|
| 📊 **Dashboard** | Estadísticas + estado de servicios | Estadísticas + estado de servicios |
| 👥 **Usuarios** | CRUD completo | ❌ Bloqueado - "Solo administradores" |
| 📦 **Productos** | CRUD completo (crear, editar, eliminar) | Solo lectura |
| 📋 **Órdenes** | CRUD completo | CRUD completo |
| 🔔 **Notificaciones** | CRUD completo | CRUD completo |
| 🏪 **Ver Tienda** | Volver a la vista pública | Volver a la vista pública |

### Credenciales de prueba

| Rol | Email | Contraseña |
|-----|-------|------------|
| **Administrador** | admin@test.com | admin123 |
| **Usuario normal** | user@test.com | user123 |

---
## Instrucciones de Despliegue

### Prerrequisitos

- Docker Desktop
- Docker Compose
- Git

### Pasos para levantar el sistema

1. Clone el repositorio:
```bash
git clone <url-del-repositorio>
cd ProyectoSoftware2
```

2. Construya y levante los contenedores:
```bash
docker compose up --build -d
```

3. Verifique que todos los servicios estén corriendo:
```bash
docker compose ps
```

4. Abra el navegador en:
```
http://localhost:3000
```

### Puertos de los Servicios

| Servicio | Puerto Interno | Puerto Externo |
|----------|---------------|----------------|
| API Gateway | 3000 | 3000 |
| Auth Service | 8000 | - (solo interno) |
| User Service | 8001 | - (solo interno) |
| Product Service | 8002 | - (solo interno) |
| Order Service | 8003 | - (solo interno) |
| Notification Service | 8004 | - (solo interno) |
| MySQL | 3306 | 3307 |
| PostgreSQL | 5432 | 5432 |
| MongoDB | 27017 | 27017 |

> **Nota:** Solo el API Gateway (puerto 3000) está expuesto al exterior. Los microservicios se comunican internamente a través de la red de Docker.

---

## Documentación de Endpoints

Todas las peticiones deben realizarse a través del **API Gateway** (`http://localhost:3000`).

### Autenticación

#### POST /auth/login
Inicia sesión con credenciales del usuario.

**Request:**
```json
{
  "email": "admin@test.com",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "success": true,
  "token": "eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tIiwicm9sZSI6ImFkbWluIiwibmFtZSI6IkFkbWluIiwiZXhwIjoxNzc4MzUyNzU2fQ==",
  "user": {
    "email": "admin@test.com",
    "role": "admin",
    "name": "Admin"
  }
}
```

**Ejemplo:**
```bash
curl -X POST http://localhost:3000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@test.com", "password": "admin123"}'
```

#### POST /auth/register
Registra un nuevo usuario en el sistema.

**Request:**
```json
{
  "name": "Nuevo Usuario",
  "email": "nuevo@test.com",
  "password": "mipassword"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Usuario registrado correctamente"
}
```

#### POST /auth/logout
Cierra la sesión del usuario.

**Request:**
```json
{
  "token": "token-de-sesion"
}
```

**Response (200):**
```json
{
  "message": "logout ok"
}
```

#### POST /auth/recover
Inicia el proceso de recuperación de contraseña.

**Request:**
```json
{
  "email": "usuario@test.com"
}
```

**Response (200):**
```json
{
  "message": "recover ok"
}
```

#### GET /auth/verify
Verifica si un token de sesión es válido.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "valid": true,
  "user": {
    "email": "admin@test.com",
    "role": "admin",
    "name": "Admin",
    "exp": 1778352756
  }
}
```

---

### Usuarios (User Service - Django)

#### GET /users
Obtiene la lista de usuarios registrados.

```bash
curl http://localhost:3000/users
```

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "Juan Pérez",
      "email": "juan@test.com",
      "role": "user",
      "status": "active"
    }
  ]
}
```

#### POST /users
Crea un nuevo usuario.

```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Nuevo", "email": "nuevo@test.com", "password": "123456", "role": "user"}'
```

#### PUT /users/:id
Actualiza un usuario existente.

```bash
curl -X PUT http://localhost:3000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Nombre Actualizado", "status": "active"}'
```

#### DELETE /users/:id
Elimina un usuario.

```bash
curl -X DELETE http://localhost:3000/users/1
```

---

### Productos (Product Service - Flask + MongoDB)

#### GET /products
Obtiene el catálogo de productos.

```bash
curl http://localhost:3000/products
```

**Response:**
```json
[
  {
    "_id": "507f1f77bcf86cd799439011",
    "name": "Laptop Gamer",
    "price": 1299.99,
    "stock": 10,
    "category": "electronica"
  }
]
```

#### POST /products
Crea un nuevo producto.

```bash
curl -X POST http://localhost:3000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Producto Nuevo", "price": 29.99, "stock": 50, "category": "general"}'
```

#### PUT /products/:id
Actualiza un producto.

```bash
curl -X PUT http://localhost:3000/products/<id> \
  -H "Content-Type: application/json" \
  -d '{"price": 19.99, "stock": 100}'
```

#### DELETE /products/:id
Elimina un producto.

```bash
curl -X DELETE http://localhost:3000/products/<id>
```

---

### Órdenes (Order Service - Express)

#### GET /orders
Obtiene la lista de órdenes.

```bash
curl http://localhost:3000/orders
```

**Response:**
```json
{
  "orders": [
    {
      "id": 1,
      "product": "Laptop Gamer",
      "quantity": 1,
      "total": 1299.99,
      "status": "pending",
      "date": "2026-05-08T18:00:00.000Z"
    }
  ]
}
```

#### POST /orders
Crea una nueva orden.

```bash
curl -X POST http://localhost:3000/orders \
  -H "Content-Type: application/json" \
  -d '{"product": "Laptop Gamer", "quantity": 1, "total": 1299.99}'
```

#### PUT /orders/:id
Actualiza una orden (ej: cambiar estado).

```bash
curl -X PUT http://localhost:3000/orders/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

#### DELETE /orders/:id
Elimina una orden.

```bash
curl -X DELETE http://localhost:3000/orders/1
```

---

### Notificaciones (Notification Service - Flask)

#### GET /notify
Obtiene todas las notificaciones.

```bash
curl http://localhost:3000/notify
```

#### POST /notify
Crea una nueva notificación.

```bash
curl -X POST http://localhost:3000/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Pedido enviado", "type": "success", "user": "general"}'
```

#### PUT /notify/:id
Actualiza una notificación.

```bash
curl -X PUT http://localhost:3000/notify/1 \
  -H "Content-Type: application/json" \
  -d '{"read": true}'
```

#### DELETE /notify/:id
Elimina una notificación.

```bash
curl -X DELETE http://localhost:3000/notify/1
```

---

### Health Check

#### GET /api/health
Verifica que el API Gateway esté funcionando.

```bash
curl http://localhost:3000/api/health
```

**Response:**
```json
{
  "status": "ok",
  "service": "API Gateway"
}
```

---

## Pruebas Unitarias (15 Tests)

El proyecto incluye **25 pruebas unitarias** distribuidas en los diferentes microservicios:

### Cómo ejecutar las pruebas

#### Tests de Django (User Service) - 5 tests
```bash
cd user-service
python manage.py test user_service.tests
```

#### Tests de Flask (Product Service) - 5 tests
```bash
cd product-service
python -m pytest test_app.py -v
```

#### Tests de Flask (Notification Service) - 5 tests
```bash
cd notification-service
python -m pytest test_app.py -v
```

#### Tests de Express (API Gateway) - 6 tests
```bash
cd api-gateway
node test_gateway.js
```

#### Tests de Express (Order Service) - 4 tests
```bash
cd order-service
node test_orders.js
```

### Resumen de tests

| Servicio | Framework | Tests | Lo que prueba |
|----------|-----------|-------|---------------|
| **User Service** | Django | 5 | Listar, crear, actualizar, eliminar usuarios + validación |
| **Product Service** | Flask | 5 | Listar, crear, actualizar, eliminar productos + validación |
| **Notification Service** | Flask | 5 | Listar, crear, actualizar, eliminar notificaciones + validación |
| **API Gateway** | Express | 6 | Health check, listar usuarios/productos/órdenes, login exitoso, login fallido |
| **Order Service** | Express | 4 | Listar, crear, actualizar, eliminar órdenes |
| **Total** | - | **25** | Supera el mínimo requerido de 15 |

---

## Pruebas de Rendimiento (Locust)

El proyecto incluye **10 pruebas de estrés** implementadas con Locust sobre diferentes endpoints del sistema.

### Instalación
```bash
pip install locust
```

### Ejecución con interfaz web
```bash
locust -f locustfile.py --host=http://localhost:3000
# Abrir http://localhost:8089
```

### Ejecución headless (sin interfaz)
```bash
# Prueba de Capacidad: 100 usuarios, 10/s, 5min
locust -f locustfile.py --host=http://localhost:3000 --headless -u 100 -r 10 -t 5m

# Prueba de Carga: 50 usuarios, 5/s, 10min
locust -f locustfile.py --host=http://localhost:3000 --headless -u 50 -r 5 -t 10m

# Prueba de Estrés: 200 usuarios, 20/s, 3min
locust -f locustfile.py --host=http://localhost:3000 --headless -u 200 -r 20 -t 3m
```

### Endpoints probados (10 pruebas de estrés)

| # | Endpoint | Método | Descripción |
|---|----------|--------|-------------|
| 1 | /auth/login | POST | Autenticación de usuarios |
| 2 | /auth/logout | POST | Cierre de sesión |
| 3 | /auth/recover | POST | Recuperación de contraseña |
| 4 | /auth/register | POST | Registro de nuevos usuarios |
| 5 | /users | GET | Listado de usuarios |
| 6 | /products | GET | Listado de productos |
| 7 | /orders | GET | Listado de órdenes |
| 8 | /notify | GET | Listado de notificaciones |
| 9 | /api/health | GET | Health check del gateway |
| 10 | /products | POST | Creación de productos |

---

## Pruebas de Seguridad

El API Gateway implementa las siguientes medidas de seguridad:

1. **Autenticación mediante tokens**: Todos los endpoints del dashboard requieren un token JWT (codificado en base64) válido.
2. **Verificación de expiración de tokens**: Los tokens expiran después de 24 horas.
3. **Control de acceso por roles**: Los usuarios normales no pueden acceder a la gestión de usuarios ni crear/editar/eliminar productos.
4. **Validación de datos**: Cada microservicio implementa su propia validación de datos de entrada.
5. **CORS**: El API Gateway configura CORS para permitir peticiones desde cualquier origen.
6. **Aislamiento de red Docker**: Los microservicios no están expuestos al exterior, solo se comunican internamente.

---

## Estructura del Proyecto

```
ProyectoSoftware2/
├── docker-compose.yml          # Orquestación de contenedores
├── locustfile.py               # Pruebas de rendimiento (10 tests de estrés)
├── README.md                   # Documentación completa
├── diagrama.png                # Diagrama de arquitectura
├── api-gateway/                # Express.js - API Gateway + Frontend
│   ├── index.js                # Enrutamiento de peticiones
│   ├── Dockerfile              # Configuración Docker
│   ├── package.json            # Dependencias
│   ├── public/
│   │   └── index.html          # Frontend web completo
│   └── test_gateway.js         # 6 tests unitarios
├── auth-service/               # Laravel - Autenticación
│   ├── app/
│   ├── routes/
│   │   └── web.php             # Endpoints de auth
│   └── Dockerfile
├── user-service/               # Django - Gestión de usuarios
│   ├── user_service/
│   │   ├── views.py            # CRUD de usuarios
│   │   ├── urls.py             # Rutas
│   │   └── tests.py            # 5 tests unitarios
│   ├── manage.py
│   └── Dockerfile
├── product-service/            # Flask + MongoDB - Productos
│   ├── app.py                  # CRUD de productos
│   ├── Dockerfile
│   └── test_app.py             # 5 tests unitarios
├── order-service/              # Express.js - Órdenes
│   ├── index.js                # CRUD de órdenes
│   ├── package.json
│   ├── Dockerfile
│   └── test_orders.js          # 4 tests unitarios
└── notification-service/       # Flask - Notificaciones
    ├── app.py                  # CRUD de notificaciones
    ├── Dockerfile
    └── test_app.py             # 5 tests unitarios
```

---

## Comandos Útiles

### Docker
```bash
# Levantar todos los servicios
docker compose up -d

# Ver logs en tiempo real
docker compose logs -f

# Detener servicios
docker compose down

# Reconstruir un servicio específico
docker compose up -d --build api-gateway

# Ver estado de los servicios
docker compose ps

# Ver logs de un servicio específico
docker compose logs api-gateway
```

### Testing
```bash
# Ejecutar todos los tests (desde dentro de cada servicio)
python manage.py test user_service.tests    # Django
python -m pytest product-service/test_app.py # Flask
node api-gateway/test_gateway.js             # Express
```

### Pruebas de estrés
```bash
locust -f locustfile.py --host=http://localhost:3000 --headless -u 200 -r 20 -t 3m
```

---

## Requisitos del Proyecto Cubiertos

| Requisito | Estado |
|-----------|--------|
| Mínimo 5 microservicios | ✅ 6 servicios (Gateway + 5 micros) |
| API Gateway como único punto de entrada | ✅ Puerto 3000 |
| Validación de datos en cada microservicio | ✅ Cada servicio valida sus datos |
| Frameworks: Laravel, Django, Flask, Express | ✅ Todos implementados |
| Bases de datos: MySQL, PostgreSQL, MongoDB | ✅ Las 3 implementadas |
| Autenticación: Login, Logout, Recuperación | ✅ Los 3 implementados |
| Frontend web con roles | ✅ Admin y User con permisos diferenciados |
| Pruebas unitarias (mínimo 15) | ✅ 25 tests implementados |
| Pruebas de rendimiento (capacidad, carga, estrés) | ✅ 10 endpoints probados |
| Pruebas de seguridad básicas | ✅ Tokens, roles, validación, CORS |
| Contenerización Docker | ✅ Todos los servicios contenerizados |
| Orquestación Docker Compose | ✅ Configuración completa |
| Diagrama de arquitectura | ✅ diagrama.png |
| Documentación de endpoints | ✅ README completo |
| README con instrucciones de despliegue | ✅ Documentación detallada |
| Repositorio GitHub público | ✅ |

---

## Licencia

Este proyecto es de uso académico para la materia de **Ingeniería de Software II**.