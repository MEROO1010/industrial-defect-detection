# industrial-defect-detection

## A real-time industrial defect detection system using YOLOv8, FastAPI, and React.

# 📌 Overview
This project provides a complete pipeline for detecting industrial defects (e.g., scratches, dents, contamination, misalignment) in real-time using a webcam or uploaded images. The system includes:
YOLOv8 model fine-tuned on the MVTec AD dataset.

Real-time inference via webcam or image upload.

Interactive confidence threshold control using a slider.

Defect logging with timestamps and images.

Statistics dashboard for daily/weekly defect rates.

Alert system for threshold breaches.

# 🛠️ Prerequisites
Python 3.9+

CUDA 11.8+ (for GPU acceleration)

Docker (for containerized deployment)

Node.js 18+ (for the React frontend)

# 📦 Installation
1. Clone the Repository
 
   ```
   git clone https://github.com/your-repo/industrial-defect-detection.git
   cd industrial-defect-detection
   ```


   
