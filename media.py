import streamlit as st
from PIL import Image
import os

path = os.path.dirname(__file__)
fichero = path+'/media/meme.jpg'
imagen = Image.open(fichero)
st.image(imagen, caption="Disaster girl meme",width=400)
st.audio(path+"/media/call-the-police-18554.mp3")
st.write('Music by [Gvidon](https://pixabay.com/users/gvidon-25326719/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=18554) from Pixabay')
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")