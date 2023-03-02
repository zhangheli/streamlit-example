import streamlit as st 
import requests 
import json
from datetime import datetime

symbol = st.text_input("symbol")
begin_time = st.text_input("begin time")
limit = st.text_input("limit", value="300")

def fetch_items(symbol, begin):
    if not symbol:
        return []

    uri = f"https://api.yshyqxx.com/api/v3/aggTrades?limit={limit}&symbol={symbol.upper()}"
    try:
        start_from =  datetime.strptime(begin, "%Y-%m-%d %H:%M:%S")
        if start_from:
            uri += f"&startTime={start_from.strftime('%s')}"
    except Exception as exp:
        st.text(f"{exp}")
        pass 
    resp = requests.get(uri).json()
    # st.text(f"uir={uri} symbol={symbol} time={begin}")

    return resp or []


result = fetch_items(symbol, begin_time)
rows = []
for x in result:
    data = dict(id=x['a'], price=x['p'], size=x['q'])
    if 'T' in x:
        data['time'] = datetime.fromtimestamp(x['T'] / 1000).strftime("%m-%d %H:%M:%S.%f")
    
    rows.append(data)


    # st.text(json.dumps(x))
st.table(rows)
