import streamlit as st

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
height:600px;
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
    top: -103px;
}

div.stButton > button:hover {
    background: transparent;
    color: #00d26a;
    transform: scale(1.05);
}
.services{
    margin-top:60px;
    padding:20px;
}

.services h2{
    text-align:center;
    color:white;
    font-size:38px;
    margin-bottom:40px;
}

.service-card{
    background:#ffffff;
    border-radius:6px;
    overflow:hidden;
    box-shadow:0 5px 15px rgba(0,0,0,.25);
    transition:.3s;
}

.service-card:hover{
    transform:translateY(-8px);
}

.service-card img{
    width:100%;
    height:180px;
    object-fit:cover;
}

.service-body{
    padding:20px;
}

.service-body h3{
    font-size:22px;
    color:#333;
    margin-bottom:15px;
}

.service-body p{
    color:#666;
    line-height:28px;
    font-size:16px;
}

.read-btn{
    display:inline-block;
    margin-top:15px;
    background:#00d26a;
    color:white;
    text-decoration:none;
    padding:10px 25px;
    border-radius:4px;
}

.read-btn:hover{
    background:#00d26a;
}
.st-emotion-cache-yn44r9 a {
    color: rgb(255 255 255);
    text-decoration: underline;
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
</style>
""", unsafe_allow_html=True)

# ---------------- Navbar ----------------

# ---------------- Navbar ----------------

logo, m1, m2, m3, m4 = st.columns([4, 1, 1, 1, 1])

st.markdown("""

        <a href="/" style="text-decoration: none; color: #00d26a; margin: 0; font-weight: bold; font-family: sans-serif;     position: relative;
    top: -36px;
    font-size: 25px;
">Kwikster
            </h2>


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

st.markdown("""
<div style="text-align:right; margin-top:-65px;">
    <a href="/login" class="login-btn">
        🔐 Login
    </a>
</div>
""", unsafe_allow_html=True)



# ---------------- Hero ----------------

st.markdown("""
<div class="hero">

<div class="overlay">

<h1>We create modern Websites, Software <br> and Web Applications to help your business succeed.</h1>

<p>
Create modern websites using Python Streamlit.
Fast, Responsive and Beautiful UI Design for your business.
</p>

<a class="btn" href="#">GET STARTED NOW</a>

</div>

</div>
""", unsafe_allow_html=True)


st.markdown("<div class='services'><h2>Our Office</h2></div>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="service-card">
        <img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=600&auto=format&fit=crop&q=80" alt="Custom Website Development">
        <div class="service-body">
            <h3>Custom Website Development</h3>
            <p>We build modern, responsive, and SEO-friendly websites tailored to your business needs.</p>
            <a href="#" class="read-btn">READ MORE</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="service-card">
        <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80" alt="Software Development">
        <div class="service-body">
            <h3>Software Development</h3>
            <p>Custom software solutions to automate your business and improve productivity.</p>
            <a href="#" class="read-btn">READ MORE</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="service-card">
        <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&auto=format&fit=crop&q=80" alt="App Development">
        <div class="service-body">
            <h3>Mobile App Development</h3>
            <p>We develop Android and iOS applications with modern UI and powerful features.</p>
            <a href="#" class="read-btn">READ MORE</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="service-card">
        <img src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=600&auto=format&fit=crop&q=80" alt="Social Media Marketing">
        <div class="service-body">
            <h3>Digital Marketing & Support</h3>
            <p>Grow your business with SEO, social media marketing, and 24/7 technical support.</p>
            <a href="#" class="read-btn">READ MORE</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

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

<p><span class="footer-icon">🌐</span> www.kwikster.com</p>

</div>

</div>

<hr style="border:1px solid #444;margin-top:35px;">

<p style="text-align:center;color:#aaa;">
© 2026 Kwikster. All Rights Reserved.
<a href="https://wseubedemo.streamlit.app/">website</a>
</p>

</div>
""", unsafe_allow_html=True)