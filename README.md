# Traffic Light Object Detection (YOLO11 + OpenCV)

Basic object detection system using **YOLO11** for detection and **OpenCV** (via Ultralytics `show=True`) to process and display video frames. Detects **Green Light** and **Red Light**.

### Setup
conda create -n yolov11_custom python=3.11 -y
conda activate yolov11_custom
pip install ultralytics opencv-python


### Train
python train.py


### Predict (video)
Place a video named traffic_lights.mp4 in the project folder (or change the path in predict.py), then run:
python predict.py


### Labels
0 = Green Light
1 = Red Light
