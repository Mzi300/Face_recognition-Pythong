

import face_recognition
import cv2

# Load an image of a person you want to recognize
known_image = face_recognition.load_image_file("Photo.png")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Create arrays for recognized person and their names
known_face_images = (known_encoding)
known_face_names = ["Mzikayise"]

# Initialize WebCam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    # Resize frame for fast processing
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1] # BGR - RGB

    # Find all faces and all face encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(face_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)

            name = known_face_names[first_match_index]

            face_names.append(name)

            # Display Results
            for(top, left, bottom, right), name in zip (face_locations, face_names):

                top *= 4
                left *= 4
                bottom *= 4
                right *= 4

            # Draw Rectangle and Label
            cv2.rectangle(frame, (top, left), (bottom, right), (0,255,0), 2)
            cv2.rectangle(frame, (top, left - 25), (bottom, right), (0,255,0),cv2.FILLED)
            cv2.putText(name, text, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0,0,0), 2)

            cv2.imshow("Face Recognition", frame)

            # Q for Quit
            if cv2.waitKey(1) & 0*FF == ord("q"):
                break

            video_capture.release()
            cv2.destroyAllWindows()












































