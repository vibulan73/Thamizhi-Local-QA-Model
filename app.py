import streamlit as st
from model_handler import get_answer
    
# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# App header
st.markdown('<div class="header">Thamizhi - QA</div>', unsafe_allow_html=True)



# Input form
context = st.text_area("Context", height=150)
question = st.text_input("Question")


if st.button("Extract Answer", type="primary"):
    if context.strip() and question.strip():
        answer = get_answer(context, question)
        st.markdown(f"""
            <div class="chat-bubble">
                <strong>Answer:</strong><br>{answer}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please input the context.")
