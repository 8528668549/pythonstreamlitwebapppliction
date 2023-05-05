import streamlit as st

# title
st.title("pyhon station")
# header
st.header("Streamlit Tutorial")
# sub header
st.subheader("Complete Streamlit Tutorial")

# text
st.text("hello everyone welcome to my python station web app Hope you like it....")

# write
st.write("please subscribe my youtube channel python station")
# image
from PIL import Image

img = Image.open("python.png")
st.image(img, caption='python station')
# colour full text
# success
st.success("success")
# error
st.error('error')

# warning
st.warning('warning')
# info
st.info("Note:You have to know this...")
# exception
st.exception('Name error(name is not define')
# help
st.help('help')
# sidebar
st.sidebar.header('about')
st.sidebar.text('''hey this is bla bla hope you like int this bla bla...if do not...''')
### widgets
# checkbox
if st.checkbox('show/hide'):
    st.write('if you like it...subscribe')
# radio
status = st.radio('what is your status', ('active', 'inactive'))
if status is 'active':
    st.success('active')
else:
    st.warning('you are in active')
# selectbox

occupation = st.selectbox('what you do for living', ['engineer', 'programmer', 'doctor', 'teacher'])
st.write('you are a', occupation)
# multiselect
location = st.multiselect("where did you live", ('india', "usa", 'japan', 'pakistan'))
st.write('you selected', len(location))

# slider
st.slider('what is your age', 21, 22)
# button
if st.button('about me'):
    st.write('hey there...myself john amir')
# text_input
gmail = st.text_input('enter your gmail id')
if '@gmail.com' in gmail:
    st.write(f'confirm your gmail id{gmail}')
# text_area
message = st.text_area('give your experience about streamlit')
# datetime
# date
import datetime

st.date_input('today is', datetime.datetime.now())
# time
import time

st.time_input('time is date', datetime.time)
# display raw code
# code
st.text('how to install streamlit')
st.code('pip install streamlit')
with st.echo():
    # how to import streamlit in your python script
    import streamlit
# display json
st.json({'name': 'amir', 'gender': 'male'})
# spinner
with st.spinner('wait a second...'):
    time.sleep(5)
    st.success('success')
# balloons
st.balloons()
