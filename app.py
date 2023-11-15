import streamlit as st
import uuid
a = uuid.getnode()
mac = ':'.join(("%012X" % a)[i:i+2] for i in range(0, 12, 2))

st.write(mac)