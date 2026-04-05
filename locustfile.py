"""
Pruebas de Rendimiento para Sistema de Microservicios

Este archivo contiene la configuración de pruebas de rendimiento utilizando Locust.
Incluye pruebas de capacidad, carga y estrés para todos los endpoints del sistema.

Para ejecutar las pruebas:
    locust -f locustfile.py --host=http://localhost:3000

Luego abra http://localhost:8089 en su navegador para configurar los parametros de la prueba.
"""

from locust import HttpUser, TaskSet, task, between
import random

class MicroservicesUser(HttpUser):
    wait_time = between(1, 3)
    
    # ============================================
    # PRUEBAS DE AUTENTICACIÓN
    # ============================================
    
    @task(3)
    def login(self):
        """Prueba de login - endpoint crítico"""
        self.client.post("/auth/login", json={
            "email": f"user{random.randint(1, 100)}@test.com",
            "password": "password123"
        }, name="/auth/login")
    
    @task(2)
    def logout(self):
        """Prueba de logout"""
        self.client.post("/auth/logout", json={
            "token": "test-token-123"
        }, name="/auth/logout")
    
    @task(1)
    def recover_password(self):
        """Prueba de recuperación de contraseña"""
        self.client.post("/auth/recover", json={
            "email": f"user{random.randint(1, 100)}@test.com"
        }, name="/auth/recover")
    
    # ============================================
    # PRUEBAS DE MICROSERVICIOS
    # ============================================
    
    @task(4)
    def get_users(self):
        """Prueba de obtención de usuarios"""
        self.client.get("/users", name="/users")
    
    @task(5)
    def get_products(self):
        """Prueba de obtención de productos"""
        self.client.get("/products", name="/products")
    
    @task(3)
    def get_orders(self):
        """Prueba de obtención de órdenes"""
        self.client.get("/orders", name="/orders")
    
    @task(2)
    def get_notify(self):
        """Prueba de notificaciones"""
        self.client.get("/notify", name="/notify")
    
    @task(1)
    def health_check(self):
        """Verificación de estado del API Gateway"""
        self.client.get("/", name="/")


# ============================================
# CONFIGURACIONES PREDEFINIDAS PARA DIFERENTES TIPOS DE PRUEBAS
# ============================================

class CapacityTestUser(MicroservicesUser):
    """
    Prueba de Capacidad:
    Determinar el límite máximo de usuarios concurrentes que el sistema puede manejar.
    
    Configuración recomendada en Locust UI:
    - Number of users: 100
    - Spawn rate: 10
    - Run time: 5m
    """
    wait_time = between(0.5, 2)


class LoadTestUser(MicroservicesUser):
    """
    Prueba de Carga:
    Evaluar el comportamiento del sistema bajo carga normal esperada.
    
    Configuración recomendada en Locust UI:
    - Number of users: 50
    - Spawn rate: 5
    - Run time: 10m
    """
    wait_time = between(2, 5)


class StressTestUser(MicroservicesUser):
    """
    Prueba de Estrés:
    Evaluar el comportamiento del sistema más allá de sus límites normales.
    
    Configuración recomendada en Locust UI:
    - Number of users: 200
    - Spawn rate: 20
    - Run time: 3m
    """
    wait_time = between(0.1, 0.5)