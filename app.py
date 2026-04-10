import streamlit as st
import hashlib
from datetime import datetime

# إعدادات الواجهة السيادية
st.set_page_config(page_title="SIGMA Sovereign System", page_icon="🛡️")

# الهوية البصرية الرسمية
st.markdown(f"""
    <div style="background-color:#002140; padding:20px; border-radius:15px; border-bottom: 5px solid #d4af37; text-align:center;">
        <h1 style="color:#d4af37;">🛡️ منصة SIGMA للحوكمة السيادية</h1>
        <p style="color:white;">المبتكر: فهد بن منصور العرجاني</p>
        <p style="color:#888; font-size:12px;">براءة اختراع رقم: PCT/SA/2026/050007</p>
    </div>
""", unsafe_allow_html=True)

st.write("\n")

# مدخلات الحوكمة (نية الإنسان مقابل مقترح الآلة)
col1, col2 = st.columns(2)
with col1:
    human_intent = st.text_area("👤 التوجيه البشري (Human Intent)", placeholder="أدخل النية البشرية هنا...")
with col2:
    ai_proposal = st.text_area("🤖 مقترح الآلة (AI Proposal)", placeholder="أدخل ما تقترحه الخوارزمية...")

if st.button("⚖️ تحليل الامتثال والسيادة"):
    if human_intent and ai_proposal:
        # ميكانيكية حساب الانحراف المعرفي CDI
        h_words = set(human_intent.lower().split())
        a_words = set(ai_proposal.lower().split())
        cdi = 1.0 - (len(h_words & a_words) / len(h_words)) if h_words else 1.0
       
        st.divider()
        st.subheader(f"📊 مؤشر الانحراف المعرفي (CDI): {round(cdi, 2)}")
       
        # بوابة الحوكمة (المادة 6.6)
        if cdi < 0.45:
            st.success("✅ APPROVED: القرار معتمد ومتوافق مع السيادة البشرية")
            token = hashlib.sha256(f"{human_intent}{ai_proposal}".encode()).hexdigest()[:16]
            st.code(f"Sovereign Token: {token}", language='text')
        else:
            st.error("❌ BLOCKED: تم حظر التنفيذ - محاولة انحراف خوارزمي عن النية")
            st.warning("تنبيه أمني: تم رصد محاولة تجاوز بوابة الحوكمة السيادية")
    else:
        st.warning("يرجى إدخال البيانات المطلوبة للتحليل.")

st.markdown("<hr><p style='text-align:center; color:grey;'>جميع الحقوق محفوظة © فهد العرجاني 2026</p>", unsafe_allow_html=True)
