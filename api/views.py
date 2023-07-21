# from django.shortcuts import render
from django.http import JsonResponse
from .face_detector_model.detector import recognize_faces
from datetime import datetime as dt
from . import sheety

sheet_id = "1efcb412e87b741c905273cf75038235/attendance"
sheet_name = "sheet1"

def upload_image_view(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']

        faces = recognize_faces(image_file)
        roll_nos = [i.split('-')[1] for i in faces]


        sheety.create_new_column()


        return JsonResponse({'message': 'Image uploaded successfully',
                             'roll_nos': roll_nos})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
