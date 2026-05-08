<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;

Route::post('/login', function (Request $request) {
    $email = $request->input('email');
    $password = $request->input('password');
    
    $users = [
        'admin@test.com' => ['password' => 'admin123', 'role' => 'admin', 'name' => 'Admin'],
        'user@test.com' => ['password' => 'user123', 'role' => 'user', 'name' => 'Usuario'],
    ];
    
    if (isset($users[$email]) && $users[$email]['password'] === $password) {
        $user = $users[$email];
        $payload = base64_encode(json_encode([
            'email' => $email,
            'role' => $user['role'],
            'name' => $user['name'],
            'exp' => time() + 86400
        ]));
        
        return response()->json([
            'success' => true,
            'token' => $payload,
            'user' => [
                'email' => $email,
                'role' => $user['role'],
                'name' => $user['name']
            ]
        ]);
    }
    
    return response()->json(['success' => false, 'message' => 'Credenciales inválidas'], 401);
});

Route::post('/register', function (Request $request) {
    return response()->json([
        'success' => true,
        'message' => 'Usuario registrado correctamente'
    ]);
});

Route::post('/logout', function () {
    return response()->json(['message' => 'logout ok']);
});

Route::post('/recover', function () {
    return response()->json(['message' => 'recover ok']);
});

Route::get('/verify', function (Request $request) {
    $token = $request->header('Authorization');
    if ($token) {
        $token = str_replace('Bearer ', '', $token);
        try {
            $data = json_decode(base64_decode($token), true);
            if ($data && isset($data['exp']) && $data['exp'] > time()) {
                return response()->json(['valid' => true, 'user' => $data]);
            }
        } catch (\Exception $e) {}
    }
    return response()->json(['valid' => false], 401);
});