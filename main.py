import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Auth System",
    page_icon="🔐",
    layout="centered"
)

# Initialize Session State for Users Data, Navigation, and Login Status
if "users_db" not in st.session_state:
    st.session_state.users_db = {}  # Temporary registration database

if "current_page" not in st.session_state:
    st.session_state.current_page = "register"  # Initial page view

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False  # Track if user is logged in

# ---------------- COMBINED CSS FOR ALL PAGES ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Dynamic Background depending on page */
.stApp {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Common Card Styling */
.auth-box {
    width: 430px;
    margin: 50px auto;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.auth-title {
    text-align: center;
    color: white;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 30px;
}

/* Input Fields styling */
.stTextInput>div>div>input {
    border-radius: 30px !important;
    height: 50px !important;
    background: rgba(255, 255, 255, 0.15) !important;
    color: black !important;
    padding-left: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
}
.stTextInput>div>div>input::placeholder {
    color: #e0e0e0 !important;
}

/* Labels and Checkbox Text */
.stTextInput label, .stCheckbox label {
    color: white !important;
}

/* Custom Buttons */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 30px !important; 
    background: linear-gradient(135deg, #00ffe7, #cb177a);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    margin-top: 20px;
    text-transform: uppercase;
    margin: 20px 0;        
    padding: 12px 37px;
}
.stButton>button:hover {
    background: linear-gradient(294deg, #c600c9, #746000);
    color: white;
}

.bottom-text {
    text-align: center;
    color: white;
    margin-top: 20px;
}
.bottom-text span {
    color: #00ffcc;
    cursor: pointer;
    font-weight: bold;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# =====================================================================
# 1. REGISTRATION PAGE
# =====================================================================
if st.session_state.current_page == "register":
    st.markdown('<style>.stApp { background: linear-gradient(135deg, #0265eb 0%, #00d2ad 100%); }</style>',
                unsafe_allow_html=True)

    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">• Register •</div>', unsafe_allow_html=True)

    reg_username = st.text_input("Choose Username", placeholder="👤 Enter username")
    reg_email = st.text_input("Email Address", placeholder="📧 Enter email")
    reg_password = st.text_input("Create Password", type="password", placeholder="🔒 Enter password")

    agree = st.checkbox("I agree to the terms and conditions")

    if st.button("Create Account"):
        if not reg_username or not reg_email or not reg_password:
            st.error("⚠️ Please fill all fields.")
        elif not agree:
            st.error("⚠️ Please accept the terms.")
        elif reg_username in st.session_state.users_db:
            st.error("❌ This username already exists! Choose another one.")
        else:
            st.session_state.users_db[reg_username] = reg_password
            st.success("🎉 Registration Successful! Redirecting to Login...")
            time.sleep(1.5)
            st.session_state.current_page = "login"
            st.rerun()

    if st.button("Already have an account? Sign In"):
        st.session_state.current_page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 2. LOGIN PAGE (Using registered data)
# =====================================================================
elif st.session_state.current_page == "login":
    st.markdown(
        '<style>.stApp { background: linear-gradient(rgba(74,200,140,.45),rgba(74,20,140,.45)), url("https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1600&q=80"); }</style>',
        unsafe_allow_html=True)

    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">Login</div>', unsafe_allow_html=True)

    login_username = st.text_input("Username", placeholder="👤 Username")
    login_password = st.text_input("Password", type="password", placeholder="🔒 Password")

    if st.button("Login"):
        if login_username in st.session_state.users_db and st.session_state.users_db[login_username] == login_password:
            st.session_state.is_logged_in = True
            st.success(f"✅ Welcome {login_username}! Login Successful.")
            time.sleep(1.5)

            # Dashboard/Home page par redirect karne ke liye path badla
            st.switch_page("pages/login.py")

        else:
            st.error("❌ Invalid Username or Password. Please try again.")

    # FIXED: type="link" ko hata diya hai error solve karne ke liye
    if st.button("Don't have an account? Register"):
        st.session_state.current_page = "register"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)