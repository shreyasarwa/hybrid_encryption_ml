import streamlit as st
import plotly.express as px
import pandas as pd

def render_analytics():
    st.markdown("<div class='glass-card'><h2>Performance Analytics</h2></div>", unsafe_allow_html=True)

    # Comparison Data
    data = {
        'Method': ['Traditional AES', 'Pure Chaos Map', 'Proposed Hybrid CNN'],
        'Accuracy': [99.9, 88.5, 98.2],
        'Time (ms)': [150, 40, 75],
        'Complexity': [9, 4, 7]
    }
    df = pd.DataFrame(data)

    c1, c2 = st.columns(2)
    with c1:
        fig_acc = px.bar(df, x='Method', y='Accuracy', color='Method', title="Accuracy Benchmark")
        st.plotly_chart(fig_acc, use_container_width=True)
    
    with c2:
        fig_time = px.line(df, x='Method', y='Time (ms)', markers=True, title="Latency Comparison")
        st.plotly_chart(fig_time, use_container_width=True)

    st.dataframe(df, use_container_width=True)