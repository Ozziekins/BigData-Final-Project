#!/bin/bash 
pip install plotly 
pip install --ignore-installed matplotlib 
pip install --ignore-installed streamlit 
 
streamlit run ../dashboard/dashboard.py --server.port 60000