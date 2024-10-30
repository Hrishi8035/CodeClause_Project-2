import cv2
import face_recognition
import os
import re  # Import regex library to handle name extraction

# Load known faces and names
known_faces = []
known_names = []

for filename in os.listdir("known_faces"):
    # Load the image and its encoding
    image = face_recognition.load_image_file(f"known_faces/{filename}")
    encoding = face_recognition.face_encodings(image)[0]
    
    # Append the encoding to known_faces
    known_faces.append(encoding)
    
    # Extract the base name by removing trailing numbers and spaces
    base_name = re.sub(r'\d+$', '', filename.split(".")[0]).strip()  # Remove numbers and trailing spaces
    known_names.append(base_name)  # All variations like "Jack 1" become "Jack"

# Initialize webcam
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to RGB for face_recognition processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, faces)

    for (top, right, bottom, left), face_encoding in zip(faces, encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # Draw bounding box and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow("Video", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
