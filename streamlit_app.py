import streamlit as st

# Set page config (optional)
st.set_page_config(page_title="Test Page", layout="centered")

# Display H1 heading
st.markdown("# test")

# Optional: embed another site (like https://snxstats.streamlit.app/)
st.markdown("---")
st.components.v1.iframe("https://snxstats.streamlit.app/", height=600, scrolling=True)
