# Facial Recognition System 

A real-time facial recognition system that uses machine learning to detect and recognize faces. This project leverages OpenCV and the face_recognition library to capture video from a webcam, recognize known faces based on pre-labeled images, and display labeled bounding boxes around identified individuals. Ideal for various applications such as security systems, attendance tracking, or simply experimenting with computer vision.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [How It Works](#how-it-works)
8. [Future Improvements](#future-improvements)
9. [Contributing](#contributing)
10. [License](#license)

---

## Overview

This Facial Recognition System project enables real-time face detection and recognition from video input using pre-trained models. Known faces are stored in a directory (`known_faces`) with associated names, making it easy to recognize familiar individuals in real-time video feeds. 

The system uses a combination of OpenCV for video capturing and `face_recognition` for efficient face detection and comparison, allowing users to add multiple images of each person for improved recognition accuracy.

## Features

- Real-time face detection and recognition.
- Simple structure: Known faces are stored in a single directory for easy updates.
- Name-based labeling using images from the `known_faces` folder.
- Allows multiple images per person to improve recognition accuracy.
- Displays bounding boxes and names around recognized faces in the video feed.

## Requirements

- Python 3.7 or higher
- OpenCV (`cv2`)
- face_recognition library
- Regex (`re`)

### Python Package Dependencies

You can install the required packages using pip:
```bash
$ pip install opencv-python face_recognition
```

## Installation

1. **Clone the Repository:**
```bash
$ git clone https://github.com/Hrishi8035/CodeClause_Project-2.git
$ cd CodeClause_Project-2
```

2. **Install Dependencies:**
```bash
$ pip install -r requirements.txt
```

3. **Prepare Known Faces:**
- In the `known_faces` directory, place images of people you want to recognize. The file names should include the person's name (e.g., John.jpg, John 1.jpg, John 2.jpg).
- The program will use these images to learn and recognize individuals in real-time.

## Usage
1. Run the program:
```bash
$ python main.py
```
2. The system will start capturing video from your webcam.
3. Recognized faces will be displayed with bounding boxes and names.
4. Press `q` to exit the video feed.

## Project Structure
- `main.py`: The main script that handles real-time video capture, face detection, and recognition.
- `known_faces/`: Directory where you store images of known individuals, labeled with names.
- `README.md`: Project documentation.
- `requirements.txt`: Lists the required Python packages.

## How It Works
1. Load Known Faces: The script reads images from the `known_faces` folder, extracts face encodings, and associates them with names. Multiple images per person improve accuracy.

2. Detect Faces in Real-Time: The system uses OpenCV to capture video and detects faces in each frame.

3. Recognize Faces: Detected faces are compared with known face encodings to find matches. Recognized faces are labeled with the corresponding name.

4. Display Output: A bounding box and label with the person's name are displayed around recognized faces in the video feed.

## Future Improvements
Some ideas for extending the project include:

- Adding face recognition using deep learning-based models for higher accuracy.
- Integrating database storage for recognized faces and logging recognized individuals.
- Implementing facial recognition from recorded video files.
- Allowing users to dynamically add new faces to the `known_faces` folder.

## Contributing
Contributions, suggestions, and improvements are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
