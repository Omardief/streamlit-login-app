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
            st.session_state.page = "Welcome"  # الصفحة الافتراضية بعد تسجيل الدخول
            st.success("تم تسجيل الدخول بنجاح!")
        else:
            st.error("اسم المستخدم أو كلمة المرور غير صحيحة")

def welcome_page():
    st.title("مرحبا بك في بايونير")
    st.write("هذه صفحة الترحيب! هنا يمكنك رؤية آخر أخبار وتحديثات بايونير.")

def registration_page():
    st.title("صفحة التسجيل")
    st.write("هنا يمكنك تسجيل حساب جديد أو تحديث بياناتك. جرب استكشاف الخيارات!")

def dashboard_page():
    st.title("لوحة التحكم")
    st.write("هذه لوحة التحكم الخاصة بك. يمكنك متابعة الإحصائيات والتقارير هنا.")

def main():
    # تهيئة حالة الجلسة
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "Welcome"

    # عرض الصفحة بناءً على حالة تسجيل الدخول
    if st.session_state.logged_in:
        # إضافة Sidebar مع Radio Buttons للتنقل
        with st.sidebar:
            st.header("القائمة")
            page = st.radio(
                "اختر الصفحة",
                ["Welcome", "Registration", "Dashboard"],
                key="page_selection",
                index=["Welcome", "Registration", "Dashboard"].index(st.session_state.page)
            )
            st.session_state.page = page
            
            # زر تسجيل الخروج في الـ Sidebar
            if st.button("تسجيل الخروج"):
                st.session_state.logged_in = False
                st.session_state.page = "Welcome"

        # عرض الصفحة بناءً على اختيار المستخدم
        if st.session_state.page == "Welcome":
            welcome_page()
        elif st.session_state.page == "Registration":
            registration_page()
        elif st.session_state.page == "Dashboard":
            dashboard_page()
    else:
        login_page()

if __name__ == "__main__":
    main()