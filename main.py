import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
st.write("MSc Physics Sheetal Yadav")
st.title('**A BLANK SPACE...A MISSING PART...**')
st.header('Python for Physics')
st.caption('Computational Physics')
st.text('Creative Thinker...')
df=pd.DataFrame({
    'x':[1,2,3] ,
    'y':[4,5,6]
})
st.dataframe(df)
st.line_chart(df)
st.area_chart(df)

fig, ax= plt.subplots()
ax.scatter(df['x'],df['y'])
st.pyplot(fig)

image= Image.open('galaxy.jpg')
st.image(image, caption='U AND I verse..')

video_file=open('../video.mp4', "rb")
video_bytes=video_file.read()
st.video(video_bytes)

