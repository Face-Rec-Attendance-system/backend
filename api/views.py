# from django.shortcuts import render
from django.http import JsonResponse
from face_detector_model.detector import recognize_faces


def upload_image_view(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']

        faces = recognize_faces(image_file)

        return JsonResponse({'message': 'Image uploaded successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
