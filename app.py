
import streamlit as st
import hashlib
from datetime import datetime

# إعدادات الواجهة السيادية (أيقونة النجمة الذهبية)
st.set_page_config(page_title="نظام SIGMA السيادي", page_icon="⭐")

# الهوية البصرية الرسمية - أسود ملكي وذهبي فخم
st.markdown(f"""
    <style>
    .main {{
        background-color: #000000;
    }}
    stTextArea textarea {{
        background-color: #1a1a1a;
        color: #d4af37;
    }}
    </style>
    <div style="background-color:#000000; padding:30px; border-radius:15px; border-bottom: 5px solid #d4af37; text-align:center;">
        <h1 style="color:#d4af37; font-size:28px; margin-bottom:10px;">⭐ نظام التفاعل السيادي الخوارزمي بين الإنسان والذكاء الاصطناعي</h1> <h2 style="color:#ffffff; font-size:20px;">المخترع والمستشار القانوني: فهد بن منصور العرجاني</h2> <p style="color:#d4af37; font-size:16px;">براءة اختراع رقم: PCT/SA/2026/050007</p>
        <p style="color:#ffffff; font-size:18px; font-weight:bold; border: 1px solid #d4af37; display: inline-block; padding: 5px 15px; border-radius: 10px;">📞 للتواصل: 0531111745</p>
    </div>
""", unsafe_allow_html=True)

st.write("\n")

# منطقة العمليات التقنية
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='color:#d4af37; text-align:center;'>👤 التوجيه البشري</h3>", unsafe_allow_html=True)
    human_intent = st.text_area("Human Intent", placeholder="أدخل نية الإنسان هنا...", label_visibility="collapsed", height=150)
with col2:
    st.markdown("<h3 style='color:#d4af37; text-align:center;'>🤖 مقترح الآلة</h3>", unsafe_allow_html=True)
    ai_proposal = st.text_area("AI Proposal", placeholder="أدخل مقترح الآلة هنا...", label_visibility="collapsed", height=150)

st.write("\n")

# زر التحليل بتصميم سيادي
if st.button("⚖️ تحليل التوافق والسيادة السيجمي"):
    if human_intent and ai_proposal:
        # حساب مؤشر الانحراف المعرفي CDI
        h_words = set(human_intent.lower().split())
        a_words = set(ai_proposal.lower().split())
        cdi = 1.0 - (len(h_words & a_words) / len(h_words)) if h_words else 1.0
       
        st.divider()
        st.markdown(f"<h2 style='text-align:center; color:#ffffff;'>📊 مؤشر الانحراف: <span style='color:#d4af37;'>{round(cdi, 2)}</span></h2>", unsafe_allow_html=True)
       
        if cdi < 0.45:
            st.success("✅ APPROVED: التفاعل معتمد سيادياً ومتوافق مع النية البشرية")
            token = hashlib.sha256(f"{human_intent}{ai_proposal}".encode()).hexdigest()[:16]
            st.code(f"Sovereign Token: {token}", language='text')
        else:
            st.error("❌ BLOCKED: تم حظر التنفيذ - رصد انحراف معرفي سيادي")
    else:
        st.warning("يرجى إدخال البيانات المطلوبة لبدء التحليل.")

st.markdown("<br><br><hr><p style='text-align:center; color:#d4af37;'>جميع الحقوق محفوظة للمخترع والمستشار القانوني © فهد العرجاني 2026</p>", unsafe_allow_html=True)

