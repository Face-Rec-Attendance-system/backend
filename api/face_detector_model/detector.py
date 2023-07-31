from django.conf import settings
import pickle
from collections import Counter
from pathlib import Path
import face_recognition


DEFAULT_ENCODINGS_PATH = Path("api/face_detector_model/models/encodings.pkl")


def recognize_faces(image, model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH):
    faces = []

    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image)

    input_face_encodings = face_recognition.face_encodings(input_image)

    for unknown_encoding in input_face_encodings:
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        faces.append(name)
    return faces


def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(loaded_encodings["encodings"], unknown_encoding)
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]
