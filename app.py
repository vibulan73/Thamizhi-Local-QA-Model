import streamlit as st
from model_handler import get_answer
    
# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# App header
st.markdown('<div class="header">🧠 தமிழ் கேள்வி - பதில் அமைப்பு</div>', unsafe_allow_html=True)



# Input form
context = st.text_area("📘 உரை", height=150)
question = st.text_input("❓ கேள்வி")


if st.button("🔍 பதிலை காண்", type="primary"):
    if context.strip() and question.strip():
        answer = get_answer(context, question)
        st.markdown(f"""
            <div class="chat-bubble">
                <strong>🤖 பதில்:</strong><br>{answer}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("தயவுசெய்து உரையும் கேள்வியும் உள்ளிடவும்.")
