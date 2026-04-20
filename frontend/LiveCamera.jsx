import React, { useRef, useEffect } from "react";

export default function LiveCamera({ onDetect }) {
  const videoRef = useRef();

  useEffect(() => {
    const video = videoRef.current;
    const stream =   navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
    const interval = setInterval(() => {
      const canvas = document.createElement("canvas");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext("2d").drawImage(video, 0, 0);
      const imageData = canvas.toDataURL("image/jpeg");
      onDetect(imageData);
    }, 100);
    return () => clearInterval(interval);
  }, []);

  return <video ref={videoRef} autoPlay playsInline />;
}