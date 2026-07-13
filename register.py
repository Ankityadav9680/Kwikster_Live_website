import streamlit as st
import time

st.set_page_config(
    page_title="Registration",
    page_icon="📝",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Hide Streamlit components */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background Gradient matching the image */
.stApp {
    background: linear-gradient(135deg, #0265eb 0%, #00d2ad 100%);
    background-size: cover;
    background-position: center;
}
.st-emotion-cache-15okssx {
    font-family: "Source Sans", sans-serif;
    font-size: 18px;
    color: inherit;
    max-width: 100%;
    overflow-wrap: break-word;
}

.st-emotion-cache-yn44r9 {
    font-family: "Source Sans", sans-serif;
    font-size: 1rem;
    margin-bottom: -1rem;
    color: rgb(244 245 249);;
    max-width: 100%;
    width: 100%;
    overflow-wrap: break-word;
}

/* Center White Card */
.registration-box {
    width: 450px;
    margin: 40px auto;
    padding: 40px;
    border-radius: 10px;
    background: #ffffff;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    position: relative;
}

/* Close Icon (X) at the top right */
.close-btn {
    position: absolute;
    top: 20px;
    right: 25px;
    color: #00d2ad;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
}

/* Registration Form Title */
.registration-title {
    text-align: center;
    color: #ffffff;
    font-size: 37px;
    font-weight: bold;
    margin-bottom: 30px;
}

/* Customizing Input Fields to look like underline style */
.stTextInput>div>div>input {
    border: none !important;
    border-bottom: 2px solid #00d2ad !important;
    border-radius: 0px !important;
    background: transparent !important;
    color: #333333 !important;
    padding-left: 10px !important;
    box-shadow: none !important;
}

.stTextInput>div>div>input:focus {
    border-bottom: 2px solid #0265eb !important;
}

/* Label styling with asterisk styling */
.stTextInput label {
    color: #fbfbfbf5 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* Checkbox Text Color */
.stCheckbox label {
    color: #ffffff !important;
    font-size: 15px !important;
}

/* Create Account Button with Gradient */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 5px;
    background: linear-gradient(90deg, #0265eb 0%, #00d2ad 100%);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: 0.3s;
    margin-top: 15px;
}

.stButton>button:hover {
    opacity: 0.9;
    color: white;
    box-shadow: 0 5px 15px rgba(2, 101, 235, 0.3);
    background: linear-gradient(90deg, #3713f9 0%, #07f1c8 100%);
}

/* Bottom Text Styling */
.bottom-text {
    text-align: center;
    color: #ffffff;
    font-size: 19px;
    margin-top: 20px;
}

.bottom-text a {
    color: #0265eb;
    text-decoration: none;
    font-weight: bold;
}

.bottom-text a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Registration Form ----------------

st.markdown('<div class="close-btn">✕</div>', unsafe_allow_html=True)
st.markdown('<div class="registration-title">• Registration Form •</div>', unsafe_allow_html=True)

# Fields
name = st.text_input("* Name")
email = st.text_input("* Email address")
country = st.text_input("Country")
phone = st.text_input("* Phone")
password = st.text_input("* Password", type="password")

# Terms and Conditions Checkbox
agree = st.checkbox("Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat.")

# Submit Button
if st.button("Create Account"):
    if name and email and phone and password and agree:
        st.success("🎉 Account Created Successfully! Redirecting to Login...")
        time.sleep(2)  # Pause for 2 seconds so the user can see the success message
        st.switch_page("pages/login.py")  # Target page location
    elif not agree:
        st.error("⚠️ Please accept the terms and conditions.")
    else:
        st.error("⚠️ Please fill in all the required fields (*).")

# Bottom link
st.markdown("""
<div class="bottom-text">
Already have an account? <a href="/login" target="_self">Sign in</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)