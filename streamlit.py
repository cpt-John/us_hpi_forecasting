import streamlit as st
import altair as alt
import pandas as pd
from streamlit_model import forecast_, get_features_info

st.set_page_config(
    page_icon="🏠", page_title="U.S. HPI Forecast App", layout="wide")


st.markdown(
    '<style>.block-container{padding-top: 1.3em;padding-bottom: 2em;}</style>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; margin-top:0; padding:0'>U.S. House Price Index Forecast</h1>",
            unsafe_allow_html=True)
st.markdown(" <p style='text-align: center'> This app predicts the data using a LSTM deep learning model \
| The data file can be found along with the source code \
| There is also an EDA notebook along with the source</p>", unsafe_allow_html=True)
st.markdown(
    """<div style='display: flex;flex-direction: row;justify-content:center'><a href="https://github.com/cpt-John/us_hpi_forecasting">\
        Source Code</a><div style='padding-inline:0.5em'> | </div><a href="https://cpt-john.github.io/">Portfolio</a></div>
    """, unsafe_allow_html=True
)
st.markdown("<hr/>", unsafe_allow_html=True)


features_info = get_features_info()
features_val = {}
[predicted_val, feature_imp_df] = [0, 0]
init_forecast = True
r1c1, r1c2, r1c3, r1c4 = st.columns((1, 1, 2, 2))

with r1c1:
    st.markdown("<h6>Current Month Variables</h6>", unsafe_allow_html=True)
with r1c2:
    st.markdown("<h6>:</h6>", unsafe_allow_html=True)

index = 1
for key, f in features_info.items():
    if index % 2:
        with r1c1:
            features_val[key] = st.slider(f["name"], min_value=f["min"],
                                          max_value=f["max"], value=f["mean"], step=f["step"],)
    else:
        with r1c2:
            features_val[key] = st.slider(f["name"], min_value=f["min"],
                                          max_value=f["max"], value=f["mean"], step=f["step"],)
    index += 1

with r1c4:
    st.markdown("<h6>Feature Importance:</h6>", unsafe_allow_html=True)

    [predicted_val, feature_imp_df] = forecast_(features_val)
    chart_data1 = feature_imp_df.T.reset_index()
    bar_chart = alt.Chart(chart_data1).properties(
        height=500,
    ).mark_bar().encode(
        x='index',
        y='value',
        color='index',
        tooltip=['index', 'value']
    ).interactive()
    st.altair_chart(bar_chart, use_container_width=True, )


with r1c3:
    st.markdown("<h6>HPI Forecsat for Next Month:</h6>",
                unsafe_allow_html=True)
    chart_data2 = pd.DataFrame(
        {"current": [features_val['HPI']], "forecasted": [predicted_val]}, index=['value']).T.reset_index()
    chart_data2 = chart_data2.round(2)
    bar_chart = alt.Chart(chart_data2).properties(
        height=500,
    ).mark_bar().encode(
        x='index',
        y='value',
        color='index',
        tooltip=['index', 'value']
    ).interactive()
    st.altair_chart(bar_chart, use_container_width=True, )
