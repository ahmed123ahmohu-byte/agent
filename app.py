import streamlit as st
import asyncio
from brain import SIMegyBrain # استيراد المحرك الذهني 
from config import AGENT_NAME # استيراد الإعدادات [cite: 9, 11]

# إعدادات الصفحة
st.set_page_config(page_title=f"{AGENT_NAME} Ultimate", page_icon="🚀", layout="wide")

# تصميم CSS مخصص ليشبه واجهة Gemini
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; padding: 10px; margin-bottom: 10px; }
    .stChatInput { border-radius: 20px; }
    h1 { color: #4285F4; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title(f"🚀 {AGENT_NAME} Ultimate Production Unit")
st.markdown("---")

# تهيئة المحرك والذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []
    
simegy = SIMegyBrain() # [cite: 12]

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# مدخلات المستخدم
if prompt := st.chat_input("بماذا يمكن لـ egysim أن يساعدك اليوم؟"):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # معالجة الطلب عبر المخ (Brain)
    with st.chat_message("assistant"):
        with st.spinner("جارٍ التحليل والإنتاج..."):
            # تشغيل المعالجة غير المتزامنة [cite: 2]
            response = asyncio.run(simegy.process_request(prompt))
            st.markdown(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})
