from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Simulamos una base de datos en memoria
users_list = [
    {'id': 1, 'name': 'Juan Pérez', 'email': 'juan@test.com', 'role': 'user', 'status': 'active'},
    {'id': 2, 'name': 'María García', 'email': 'maria@test.com', 'role': 'user', 'status': 'active'},
    {'id': 3, 'name': 'Admin Sistema', 'email': 'admin@test.com', 'role': 'admin', 'status': 'active'},
]
next_id = 4

@csrf_exempt
def users(request):
    global next_id, users_list
    if request.method == 'GET':
        return JsonResponse({'users': users_list})
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            data = {}
        user = {
            'id': next_id,
            'name': data.get('name', ''),
            'email': data.get('email', ''),
            'role': data.get('role', 'user'),
            'status': data.get('status', 'active')
        }
        next_id += 1
        users_list.append(user)
        return JsonResponse(user, status=201)

@csrf_exempt
def user_detail(request, id):
    global users_list
    user = next((u for u in users_list if u['id'] == id), None)
    if not user:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse(user)
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except:
            data = {}
        for field in ['name', 'email', 'role', 'status']:
            if field in data:
                user[field] = data[field]
        return JsonResponse(user)
    
    elif request.method == 'DELETE':
        users_list = [u for u in users_list if u['id'] != id]
        return JsonResponse({'message': 'User deleted'})