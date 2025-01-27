import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


conn = st.connection('mysql', type='sql')

df = conn.query('SELECT * from SELECT * FROM restaurants;', ttl=600)

st.write(df)