from fastapi import FastAPI, WebSocket, UploadFile
from fastapi.staticfiles import StaticFiles
from detector import DefectDetector
import cv2
import base64
import asyncio

app = FastAPI()
detector = DefectDetector()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        frame = base64.b64decode(data)
        frame = cv2.imdecode(np.frombuffer(frame, np.uint8), cv2.IMREAD_COLOR)
        results = detector.detect(frame)
        await websocket.send_json(results.to_json())

@app.post("/upload")
async def upload_image(file: UploadFile):
    frame = cv2.imdecode(await file.read(), cv2.IMREAD_COLOR)
    results = detector.detect(frame)
    return results.to_json()

app.mount("/", StaticFiles(directory="frontend/build"), name="frontend")