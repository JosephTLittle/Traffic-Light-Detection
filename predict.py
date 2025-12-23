from ultralytics import YOLO

model = YOLO("yolov11_custom.pt")

VIDEO_PATH = "traffic_lights.mp4"  # put your own video here

model.predict(source = VIDEO_PATH, show = True, save = True, conf=0.7,
	line_width = 2, save_crop = False, save_txt = False, show_labels = True, 
	show_conf = True, classes = [0,1])
