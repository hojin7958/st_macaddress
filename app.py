import streamlit as st
import uuid
from pywinauto import findwindows


a = uuid.getnode()
mac = ':'.join(("%012X" % a)[i:i+2] for i in range(0, 12, 2))


for i in findwindows.find_elements():
    print(i)


st.write(mac)