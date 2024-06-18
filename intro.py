import streamlit as st
import pandas as pd
import numpy as np
import re
from datetime import datetime
#import io


st.title("SAP SAM Log Parser")
uploaded_file=st.file_uploader("Upload a SAM file")
st.write("---")
if uploaded_file is not None:
    

    # Read the file line by line
    start = ""
    end = ""
    batchStart = ""
    batchEnd = ""

    for lineB in uploaded_file.readlines():
        # Search for the pattern in the line
        line=lineB.decode('utf-8')
        match = re.search('#(.*): DEBUG .* subset complete.', line)
        if match:
            batchStart = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object

        match = re.search('#(.*): DEBUG .* PMMobileStatuses\?\$filter=MobileStatus eq \'STARTED\' and Status eq \'WORKORDER: STARTED\', headers = , payloadType = PAYLOAD_EMPTY', line)
        if match:
            start = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object

        match = re.search('#(.*): DEBUG .* Background transfer information: .* bytes were downloaded using background synchronization.', line)
        if match:
            batchEnd = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object

        match = re.search('#(.*): DEBUG .* request method = METHOD_GET, url = ErrorArchive, headers = , payloadType = PAYLOAD_EMPTY', line)
        if match:
            end = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S:%f %z')  # Convert to datetime object
            if (start != ""):
                print("start: " + str(start))  # Print datetime object as string
                print("\tbatchStart: " + str(batchStart))  # Print datetime object as string
                print("\tbatchEnd: " + str(batchEnd))  # Print datetime object as string
                print("\tdelta: ",(batchEnd-batchStart).total_seconds())
                print("end: " + str(end))  # Print datetime object as string
                st.text("start: " + str(start) +"\n\tbatchStart: " + str(batchStart) + "\n\tbatchEnd: " + str(batchEnd) + "\n\tdelta: "+str((batchEnd-batchStart).total_seconds()) + "\nend: " + str(end)) 
            start = ""
            end = ""
            batchStart = ""
            batchEnd = ""



