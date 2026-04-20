import cv2
import torch
from ultralytics import YOLO

class DefectDetector:
    def __init__(self, model_path="yolov8_mvtec_ad.pt"):
        self.model = YOLO(model_path)
        self.confidence_threshold = 0.5

    def detect(self, frame):
        results = self.model(
            frame,
            conf=self.confidence_threshold,
            device="0" if torch.cuda.is_available() else "cpu"
        )
        return results

    def set_confidence_threshold(self, threshold):
        self.confidence_threshold = threshold