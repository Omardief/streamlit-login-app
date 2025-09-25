import streamlit as st

# تحديد بيانات تسجيل الدخول كمتغيرات
USERNAME = "admin"
PASSWORD = "password123"

def login_page():
    st.title("صفحة تسجيل الدخول")
    
    # إنشاء حقول إدخال اسم المستخدم وكلمة المرور
    username_input = st.text_input("اسم المستخدم", key="username")
    password_input = st.text_input("كلمة المرور", type="password", key="password")
    
    # زر تسجيل الدخول
    if st.button("تسجيل الدخول"):
        if username_input == USERNAME and password_input == PASSWORD:
            st.session_state.logged_in = True
            st.success("تم تسجيل الدخول بنجاح!")
        else:
            st.error("اسم المستخدم أو كلمة المرور غير صحيحة")

def welcome_page():
    st.title("مرحبا بك في بايونير")
    if st.button("تسجيل الخروج"):
        st.session_state.logged_in = False

def main():
    # تهيئة حالة الجلسة
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # عرض الصفحة بناءً على حالة تسجيل الدخول
    if st.session_state.logged_in:
        welcome_page()
    else:
        login_page()

if __name__ == "__main__":
    main()