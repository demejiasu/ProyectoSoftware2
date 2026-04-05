<?php

use Illuminate\Support\Facades\Route;

Route::post('/login', function () {
    return response()->json(['message' => 'login ok']);
});

Route::post('/logout', function () {
    return response()->json(['message' => 'logout ok']);
});

Route::post('/recover', function () {
    return response()->json(['message' => 'recover ok']);
});