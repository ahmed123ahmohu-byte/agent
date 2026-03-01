import streamlit as st
import asyncio
from brain import SIMegyBrain
from config import AGENT_NAME, LOCAL_MODEL_NAME

# إعداد هوية egysim البصرية
st.set_page_config(page_title=f"{AGENT_NAME} Ultimate", page_icon="🎨", layout="wide")

# تخصيص الواجهة لتكون "أعلى من العليا"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stChatMessage { border: 1px solid #30363d; border-radius: 10px; background: #161b22; }
    .stChatInputContainer { padding-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# تهيئة المحرك
if "simegy" not in st.session_state:
    st.session_state.simegy = SIMegyBrain()
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title(f"🛸 {AGENT_NAME} Ultimate Dashboard")
st.caption(f"محرك الإنتاج المتكامل متصل عبر نموذج: {LOCAL_MODEL_NAME}")

# عرض سجل المحادثة الإبداعي
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# استقبال الأوامر الإبداعية
if prompt := st.chat_input("بماذا يمكن لـ egysim أن يبهرك اليوم؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🧠 جارٍ التحليل، التخطيط، ثم التنفيذ..."):
            # استدعاء المخ لمعالجة الطلب محلياً [cite: 1, 5]
            response = asyncio.run(st.session_state.simegy.process_request(prompt))
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
