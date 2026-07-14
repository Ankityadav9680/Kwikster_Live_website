import streamlit as st
import time

st.set_page_config(
    page_title="Startup Website",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Hide Streamlit default menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
    background:#0d1b2a;
}

/* Navbar */

.navbar{
display:flex;
justify-content:space-between;
align-items:center;
background:#1b263b;
padding:18px 60px;
border-radius:10px;
}

.logo{
font-size:32px;
font-weight:bold;
color:white;
}

.logo span{
color:#00d26a;
}

.menu a{
text-decoration:none;
color:white;
margin-left:25px;
font-size:16px;
font-weight:bold;
position: relative;
left: -537px;
}

.menu a:hover{
color:#00d26a;
}

/* Hero */

.hero{
background-image:url("https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1600&q=80");
background-size:cover;
background-position:center;
height:684px;
border-radius:12px;
position:relative;
overflow:hidden;
margin-top:20px;
}

.overlay{
background:rgba(0,0,0,.55);
height:100%;
padding:120px 80px;
}

.overlay h1{
font-size:65px;
color:white;
margin-bottom:20px;
}

.overlay p{
font-size:20px;
color:#ddd;
width:550px;
line-height:35px;
}

.btn{
display:inline-block;
background:#00d26a;
padding:15px 35px;
margin-top:30px;
border-radius:8px;
text-decoration:none;
color:white;
font-weight:bold;
}

/* About */

.about{
padding:60px;
border-radius:10px;
margin-top:50px;
text-align:center;
}

.about h2{
font-size:42px;
color:#ffff;
}

.about p{
font-size:20px;
line-height:35px;
color:#ffff;
}

/* Cards */

.card{
background:white;
padding:35px;
border-radius:12px;
text-align:center;
box-shadow:0 10px 20px rgba(0,0,0,.15);
transition:.4s;
height:230px;
}

.card:hover{
transform:translateY(-10px);
background:#00d26a;
color:white;
}

.card h3{
font-size:28px;
}

.card p{
font-size:18px;
}

/* Contact */

.contact{
background:white;
padding:50px;
border-radius:10px;
margin-top:40px;
}

/* Footer */

.footer{
margin-top:40px;
background:#1b263b;
padding:25px;
text-align:center;
color:white;
border-radius:10px;
}

/* ================= FOOTER ================= */

.footer{
    background:#0d1b2a;
    color:white;
    padding:60px 50px;
    margin-top:60px;
    border-radius:10px;
}

.footer h3{
    color:white;
    margin-bottom:20px;
    font-size:22px;
}

.footer p{
    color:#bdbdbd;
    line-height:28px;
    font-size:15px;
}

.footer a{
    color:#bdbdbd;
    text-decoration:none;
    display:block;
    margin-bottom:12px;
    transition:.3s;
}

.footer a:hover{
    color: rgb(0, 210, 106);
    padding-left:8px;
}

.footer ul{
    list-style:none;
    padding:0;
}

.footer li{
    margin-bottom:12px;
    color:#bdbdbd;
}

.footer-icon{
    color:#f9a826;
    margin-right:10px;
    font-weight:bold;
}
div.stButton > button {
    background: transparent;
    color: #ffff;
    border: none;
    border-radius: 10px;
    padding: 10px 30px;
    font-size: 25px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
    position: relative;
    right: -413px;
    top: -160px;
    box-shadow: none;
}
.st-emotion-cache-15okssx {
    font-family: "Source Sans", sans-serif;
    font-size: 17px;
    color: inherit;
    max-width: 100%;
    overflow-wrap: break-word;
}
.st-emotion-cache-3pwa5w {
    width: 100%;
    height: auto;
    text-align: left;
    max-width: 100%;
    min-width: 1rem;
    position: relative;
    overflow: visible;
    position: relative;
    top: -121px;
}

div.stButton > button:hover {
    background: transparent;
    color: #00d26a;
    transform: scale(1.05);
}

/* Sahi Navigation Buttons Styling */
div.stButton > button {
    color: #ffff;
    border: none;
    border-radius: 5px;
    padding: 5px 15px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
    width: 100%; /* Column ki width fit karne ke liye */
    margin-top: 15px; /* Logo ke sath align karne ke liye */
    position: relative;
    top: -92px;
    left: -356px;
}

div.stButton > button:hover {
    background: rgba(255, 255, 255, 0.1);
    color: #00d26a;
    transform: scale(1.05);
}

.login-btn{
    display:inline-block;
    background:linear-gradient(135deg,#00d26a,#00a854);
    color:#ffff;
    text-decoration:none;
    padding:12px 28px;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
    transition:all .3s ease;
    box-shadow:0 8px 20px rgba(0,210,106,.35);
    position: relative;
    top: -29px;
}

.login-btn:hover{
    background:linear-gradient(135deg,#00a854,#008f46);
    color:#fff;
    transform:translateY(-3px);
    box-shadow:0 12px 25px rgba(0,210,106,.45);
}

.login-btn:active{
    transform:scale(.96);
}

.st-emotion-cache-yn44r9 a {
    color: rgb(229 229 229);
    text-decoration: underline;
}

/* Logout button style modification */
.logout-container {
    text-align: right; 
    margin-top: -150px; 
    position: relative; 
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Navbar ----------------

logo, m1, m2, m3, m4, auth_col = st.columns([4, 1, 1, 1, 1, 1.5])

st.markdown("""
        <a href="/" style="text-decoration: none; color: #00d26a; margin: 0; font-weight: bold; font-family: sans-serif;     position: relative;
    top: -36px;
    font-size: 25px;
">Kwikster</a>
""", unsafe_allow_html=True)

with m1:
    if st.button("Home"):
        st.switch_page("pages/Home.py")

with m2:
    if st.button("About"):
        st.switch_page("pages/about.py")

with m3:
    if st.button("Server"):
        st.switch_page("pages/server.py")

with m4:
    if st.button("Gallery"):
        st.switch_page("pages/glarry.py")

# --- Dynamic Login/Logout Button Logic ---
with auth_col:
    # Check karein agar user already logged in hai
    if "is_logged_in" in st.session_state and st.session_state.is_logged_in:
        st.markdown('<div class="logout-container">', unsafe_allow_html=True)
        if st.button("🔓 Logout", type="secondary"):
            st.session_state.is_logged_in = False
            st.session_state.current_page = "register" # State ko register kar diya
            st.success("Logout Successful! Redirecting to Register...")
            time.sleep(1)
            st.switch_page("main.py") # <--- Register page par redirect karne ke liye path set kiya
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Agar logged in nahi hai toh normal login link dikhega
        st.markdown("""
        <div style="text-align:right; margin-top:-150px;">
            <a href="/login" target="_self" class="login-btn" style="text-decoration: none; font-size: 16px;">
                🔐 Login
            </a>
        </div>
        """, unsafe_allow_html=True)


# ---------------- Hero ----------------

st.markdown("""
<div class="hero">

<div class="overlay">

<h1>Take Your Business to the Digital World <br> Contact us today to get your professional <br>Website or Software developed</h1>

<p>
From stunning Websites to powerful Business Software, we build solutions that drive growth. Let's create something amazing together.
</p>

<a class="btn" href="#">GET STARTED NOW</a>

</div>

</div>
""", unsafe_allow_html=True)

# ---------------- About ----------------

st.markdown("""
<div class="about">
  <h2>About Us</h2>
  <p>
    We provide Website Development, Python Development,
    Artificial Intelligence, Machine Learning,
    Dashboard Development and Professional Business Solutions.
  </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 6 cards in two rows of three
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown("""
    <div class="card">
      <h3>🖥️</h3>
      <h3>HTML</h3>
      <p>Responsive Website Development</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="card">
      <h3>🎨</h3>
      <h3>CSS</h3>
      <p>Modern, adaptive UI styling</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="card">
      <h3>📦</h3>
      <h3>JavaScript</h3>
      <p>Interactive front-end experiences</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("""
    <div class="card">
      <h3>🐍</h3>
      <h3>Python</h3>
      <p>APIs, automation & back-end services</p>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="card">
      <h3>🤖</h3>
      <h3>AI & ML</h3>
      <p>Intelligent models & data-driven solutions</p>
    </div>
    """, unsafe_allow_html=True)

with row2_col3:
    st.markdown("""
    <div class="card">
      <h3>📊</h3>
      <h3>Dashboards</h3>
      <p>Analytics dashboards & BI reporting</p>
    </div>
    """, unsafe_allow_html=True)


st.write("")

st.markdown("""
<div class="footer">

<div style="display:flex;justify-content:space-between;gap:40px;flex-wrap:wrap;">

<div style="flex:1;min-width:250px;">
<h3>ABOUT US</h3>

<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vivamus vel lacus nec sapien luctus volutpat.
Suspendisse potenti. Integer euismod, libero at
consequat dignissim, lorem nisl tincidunt elit,
ut posuere massa ipsum vitae neque.
</p>

</div>

<div style="flex:1;min-width:220px;">

<h3>QUICK LINKS</h3>

<a href="#">➜ ALL SERVICES</a>
<a href="#">➜ ABOUT COMPANY</a>
<a href="#">➜ PRICING PLANS</a>
<a href="#">➜ SPECIAL OFFERS</a>
<a href="#">➜ CONTACT US</a>

</div>

<div style="flex:1;min-width:250px;">

<h3>GET IN TOUCH</h3>

<p><span class="footer-icon">📍</span>Mansarovar, Jaipur, <br>Rajasthan 302020</p>

<p><span class="footer-icon">📞</span> +91 9680585299</p>

<p><span class="footer-icon">✉️</span> info@kwikster.com</p>

<p><span class="footer-icon">🌐</span> Ankityadav303711@gmail.com</p>

</div>

</div>

<hr style="border:1px solid #444;margin-top:35px;">

<p style="text-align:center;color:#aaa;">
© 2026 Kwikster. All Rights Reserved.
<a href="https://wseubedemo.streamlit.app/">website</a>
</p>

</div>
""", unsafe_allow_html=True)