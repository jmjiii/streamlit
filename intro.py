import streamlit as st
import pandas as pd
import numpy as np
import re
from datetime import datetime
from io import StringIO

st.write("Hello World!")
st.title("SAP SAM Log Parser")
st.header("Header")
st.text("general text")
st.markdown("**bold text** *italic text*")
st.markdown("---")

uploaded_file=st.file_uploader("Upload a SAM file")
if uploaded_file:
    
    st.write(uploaded_file.name)
    st.write(uploaded_file.type)
    st.write(uploaded_file.size)
    
    # Read the file line by line
    start = ""
    end = ""
    batchStart = ""
    batchEnd = ""

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    for line in string_data:


    # To convert to a string based IO:

    
        # Search for the pattern in the line
        match = re.search('#(.*): DEBUG .* subset complete.', line)
        if match:
            batchStart = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object
            next  # Remove this line, it's not needed

        match = re.search('#(.*): DEBUG .* PMMobileStatuses\?\$filter=MobileStatus eq \'STARTED\' and Status eq \'WORKORDER: STARTED\', headers = , payloadType = PAYLOAD_EMPTY', line)
        if match:
            start = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object
            next  # Remove this line, it's not needed

        match = re.search('#(.*): DEBUG .* Background transfer information: .* bytes were downloaded using background synchronization.', line)
        if match:
            batchEnd = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object
            next  # Remove this line, it's not needed

        match = re.search('#(.*): DEBUG .* request method = METHOD_GET, url = ErrorArchive, headers = , payloadType = PAYLOAD_EMPTY', line)
        if match:
            end = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object
            if (start != ""):
                print("start: " + str(start))  # Print datetime object as string
                print("\tbatchStart: " + str(batchStart))  # Print datetime object as string
                print("\tbatchEnd: " + str(batchEnd))  # Print datetime object as string
                print("\tdelta: ",(batchEnd-batchStart).total_seconds())
                print("end: " + str(end))  # Print datetime object as string
            start = ""
            end = ""
            batchStart = ""
            batchEnd = ""
            next  # Remove this line, it's not needed


st.metric(label="speed", value=100, delta=10)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
st.table(df)
st.dataframe(df)

state=st.checkbox("Checkbox1",value=True,key="check1" )
if state:
    st.write("Checkbox1 is checked")
else:
    st.write("Checkbox1 is not checked")

def change():
    if 'check2' not in st.session_state:
        st.session_state['check2'] = True
    print(st.session_state.check2)
state2=st.checkbox("Checkbox2",value=True, on_change=change(),key="check2" )

radio_btn=st.radio("Russian Radio",options={"US","UK","Russia"})
print(radio_btn)

def btnClick():
    print("Button Clicked")

btn=st.button("Submit",on_click=btnClick)

def selectChange():
    print("Select Changed")

select=st.selectbox("Select",options=["US","UK","Russia"], on_change=selectChange())
multi_select=st.multiselect("Favorite food",options=["Apple","Banana","Orange"])
print(multi_select)

