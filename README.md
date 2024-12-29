# Animal Detection Project

## Overview
This project uses machine learning to detect animals in images using a pre-trained model. It has a graphical user interface (GUI) built with Tkinter to interact with the user.

## Installation

To install this project and its dependencies, follow the steps below:

1. Clone the repository or download the project folder.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python front.py
    ```

## Files

- `front.py`: The GUI frontend for the application.
- `anidetect.py`: The script that runs the animal detection model.
- `coco_labels.txt`: Contains the class labels for object detection.
- `ssd_mobilenet_v2_coco/`: Directory containing the trained model.
- `background.jpg`: Background image used in the GUI.
- `click.wav`: Sound played when the button is clicked.

## Usage
Click the "Start Detection" button to run the animal detection process. You will see the results displayed in a message box.

## License
MIT License
