from django.http import JsonResponse

def users(request):
    return JsonResponse({"users": []})