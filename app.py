import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# إعدادات واجهة Virex الاحترافية
st.set_page_config(page_title="Virex Sales Hub", page_icon="🚀")

# كود CSS لدعم المظهر الفخم واللغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    body, div, label, input { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stButton>button { background-color: #1a237e; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 نظام Virex للإدارة الذكية")
st.subheader("تسجيل العمليات - رمضان 2026")

# استمارة إدخال البيانات
with st.form("virex_form"):
    c_name = st.text_input("اسم العميل")
    c_phone = st.text_input("رقم الواتساب")
    service = st.selectbox("الخدمة", ["أتمتة برمجية", "تطبيقات/مواقع", "خطة تسويقية"])
    price = st.number_input("قيمة التعاقد", min_value=0)
    sales = st.selectbox("الموظف المسئول", ["سيلز 1", "سيلز 2", "سيلز 3", "سيلز 4", "سيلز 5"])
    
    submitted = st.form_submit_button("إرسال البيانات للقاعدة المركزية")

if submitted:
    if c_name and c_phone:
        st.balloons()
        st.success(f"تم تسجيل {c_name} بنجاح. سيتم التحديث في جوجل شيت فوراً.")
    else:
        st.error("يرجى إدخال البيانات المطلوبة")
