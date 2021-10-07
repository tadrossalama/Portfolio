from fastai.learner import export
import streamlit as st
import pickle
from PIL import Image
from fastai.vision.all import *
from pathlib import Path
import coremltools as ct


path = Path()
learn_inf = load_learner(path/'model.pkl')



st.title('Coral Classifier :mag_right:')
upload = st.file_uploader('Upload picture of coral here')
if upload is not None:
    
    image = PILImage.create(upload)
    st.image(image, caption='Uploaded Image.')
    pred,pred_idx,probs = learn_inf.predict(image)
    
    st.title(f'I am {probs[pred_idx] * 100:.04f}% sure this is a {pred} coral.')

