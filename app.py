

#import module

import numpy as np
import cv2

import streamlit as st
import tensorflow as tf
import keras
from tensorflow import keras
import av
from keras.preprocessing.image import img_to_array
from streamlit_webrtc import webrtc_streamer,VideoTransformerBase,RTCConfiguration,VideoProcessorBase,WebRtcMode




try:
	face_cascade= cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml') # Face Detection
except Exception:
	st.write("Error loading cascade classifiers")

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

class EmotionProcessor:
	def recv(self, frame):
		img = frame.to_ndarray(format="bgr24")
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(
                image=img_gray, scaleFactor=1.3, minNeighbors=5)
                
                for (x, y, w, h) in faces:
			cv2.rectangle(img=img, pt1=(x, y), pt2=((x + w), y + h), color=(255, 0, 0), thickness=2)
                return av.VideoFrame.from_ndarray(img, format="bgr24")
  
  
def main():
	st.title('Facial Emotion Detection :-')
        activity= ["Home", "Detect the emotion", "About the project"]
        choice = st.sidebar.selectbox("Choose the option", activity)
        if(choice=='Home'):
		st.write('hello')
        elif(choice=='Detect the emotion'):
		webrtc_streamer(key="key",mode=WebRtcMode.SENDRECV,
				video_processor_factory=EmotionProcessor,rtc_configuration=RTC_CONFIGURATION,media_stream_constraints={
            "video": True,
            "audio": False 
        },async_processing=True)

if __name__=='__main__':
	main()
