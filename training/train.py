import torch
from ultralytics import YOLO
from ultralytics.data.augment import Augmenter

def train_model():
    # تحميل النموذج
    model = YOLO("yolov8n.pt")

    # تضخيم البيانات
    augmenter = Augmenter(
        hflip=0.5,
        vflip=0.5,
        rotate=0.2,
        scale=0.1,
        mosaic=0.5
    )

    # تدريب
    results = model.train(
        data="mvtec_ad.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        augmenter=augmenter,
        device="0" if torch.cuda.is_available() else "cpu"
    )

    # حفظ النموذج
    model.save("yolov8_mvtec_ad.pt")

if __name__ == "__main__":
    train_model()