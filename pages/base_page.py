import streamlit as st
import pandas as pd
import time
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

def app():
    st.title('TS - Data refactoring')
    st.write('---')
    file = st.file_uploader('Please attach the master file updated:')
    if file:
        df = pd.read_excel(file)
        with st.expander('Data Analysis:'):
            profile_report = st.button('Generate profile report')
            if profile_report:
                pr = df.profile_report()
                st_profile_report(pr)

        with st.expander('Price adjustment:'):
            st.subheader('Adjust price by Supplier:')
            adjustment = {}
            for supplier in set(df['Proveedor (para info interna HOMEXPRESS)'].unique()):
                c1, c2 = st.columns(2)
                with c1:
                    st.write(supplier)
                with c2:
                    a = st.number_input('Percentaje of adjustment', key=f'{supplier}')
                adjustment[supplier] = a
                st.write('---')
            st.write(adjustment)