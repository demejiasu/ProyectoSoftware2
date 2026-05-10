"""
Pruebas de Rendimiento para Sistema de Microservicios
Incluye pruebas de capacidad, carga y estrés (10 endpoints).

Ejecución:
    locust -f locustfile.py --host=http://localhost:3000
    locust -f locustfile.py --host=http://localhost:3000 --headless -u 100 -r 10 -t 5m
"""

from locust import HttpUser, TaskSet, task, between
import random
import json

class MicroservicesUser(HttpUser):
    wait_time = between(1, 3)

    # ============================================
    # 10 PRUEBAS DE ESTRÉS SOBRE DIFERENTES ENDPOINTS
    # ============================================

    @task(3)
    def test_1_login_stress(self):
        """1. Estrés en autenticación - POST /auth/login"""
        self.client.post("/auth/login", json={
            "email": f"user{random.randint(1, 100)}@test.com",
            "password": "password123"
        }, name="[ESTRÉS] POST /auth/login")

    @task(2)
    def test_2_logout_stress(self):
        """2. Estrés en cierre de sesión - POST /auth/logout"""
        self.client.post("/auth/logout", json={
            "token": "test-token-123"
        }, name="[ESTRÉS] POST /auth/logout")

    @task(1)
    def test_3_recover_stress(self):
        """3. Estrés en recuperación de contraseña - POST /auth/recover"""
        self.client.post("/auth/recover", json={
            "email": f"user{random.randint(1, 100)}@test.com"
        }, name="[ESTRÉS] POST /auth/recover")

    @task(4)
    def test_4_register_stress(self):
        """4. Estrés en registro - POST /auth/register"""
        self.client.post("/auth/register", json={
            "name": "Test User",
            "email": f"test{random.randint(1, 1000)}@test.com",
            "password": "test123"
        }, name="[ESTRÉS] POST /auth/register")

    @task(5)
    def test_5_get_users_stress(self):
        """5. Estrés en listar usuarios - GET /users"""
        self.client.get("/users", name="[ESTRÉS] GET /users")

    @task(6)
    def test_6_get_products_stress(self):
        """6. Estrés en listar productos - GET /products"""
        self.client.get("/products", name="[ESTRÉS] GET /products")

    @task(3)
    def test_7_get_orders_stress(self):
        """7. Estrés en listar órdenes - GET /orders"""
        self.client.get("/orders", name="[ESTRÉS] GET /orders")

    @task(2)
    def test_8_get_notifications_stress(self):
        """8. Estrés en notificaciones - GET /notify"""
        self.client.get("/notify", name="[ESTRÉS] GET /notify")

    @task(1)
    def test_9_health_check_stress(self):
        """9. Estrés en health check - GET /api/health"""
        self.client.get("/api/health", name="[ESTRÉS] GET /api/health")

    @task(2)
    def test_10_create_product_stress(self):
        """10. Estrés en creación de producto - POST /products"""
        self.client.post("/products", json={
            "name": f"Product {random.randint(1, 1000)}",
            "price": round(random.uniform(5, 500), 2),
            "stock": random.randint(1, 100),
            "category": random.choice(["electronica", "ropa", "hogar", "deportes"])
        }, name="[ESTRÉS] POST /products")


# ============================================
# PRUEBAS DE CAPACIDAD
# ============================================
class CapacityTestUser(MicroservicesUser):
    """
    Prueba de Capacidad: 100 usuarios, 10/s, 5min
    Determinar el límite máximo de usuarios concurrentes.
    """
    wait_time = between(0.5, 2)


# ============================================
# PRUEBAS DE CARGA
# ============================================
class LoadTestUser(MicroservicesUser):
    """
    Prueba de Carga: 50 usuarios, 5/s, 10min
    Evaluar comportamiento bajo carga normal esperada.
    """
    wait_time = between(2, 5)


# ============================================
# PRUEBAS DE ESTRÉS
# ============================================
class StressTestUser(MicroservicesUser):
    """
    Prueba de Estrés: 200 usuarios, 20/s, 3min
    Evaluar comportamiento más allá de los límites normales.
    """
    wait_time = between(0.1, 0.5)