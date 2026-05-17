# =========================================================
# NOVAMIND AI - ULTIMATE STARTUP SUCCESS PREDICTION
# =========================================================

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import joblib
import requests
import time
from streamlit_lottie import st_lottie

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NovaMind AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# INITIALIZE SESSION STATE FOR SEQUENTIAL FLOW
# =========================================================
if "diagnostics_run" not in st.session_state:
    st.session_state.diagnostics_run = False

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_prediction_model():
    try:
        return joblib.load("startup_success_model.pkl")
    except FileNotFoundError:
        return None

model = load_prediction_model()

# =========================================================
# LOTTIE FUNCTION
# =========================================================

def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

lottie_ai = load_lottie("https://assets5.lottiefiles.com/packages/lf20_iorpbol0.json")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
    color:white;
}

.stApp{
    background:
    radial-gradient(circle at top left,#06b6d455,transparent 25%),
    radial-gradient(circle at bottom right,#8b5cf655,transparent 25%),
    radial-gradient(circle at center,#ec489955,transparent 20%),
    linear-gradient(135deg,#020617,#071427,#0f172a,#111827);

    background-size:400% 400%;
    animation:bgMove 15s ease infinite;
}

.hero-title{
    font-size:88px;
    font-weight:900;
    font-family:Orbitron;
    background: linear-gradient(90deg, #ffffff, #06b6d4, #8b5cf6, #ec4899);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub{
    font-size:22px;
    color:#dbeafe;
    margin-top:18px;
    line-height:1.8;
}

.glass{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(25px);
    border-radius:28px;
    padding:24px;
    box-shadow: 0px 12px 35px rgba(0,0,0,0.35);
    transition:0.4s;
}

.glass:hover{
    transform:translateY(-6px);
    border:1px solid rgba(6,182,212,0.35);
    box-shadow: 0px 0px 22px rgba(6,182,212,0.15);
}

.result-display-card {
    padding:18px;
    border-radius:18px;
    margin-top:20px;
    text-align:center;
    font-size:22px;
    font-weight:700;
    border:1px solid rgba(255,255,255,0.08);
}

.result-percentage-text {
    background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899);
    -webkit-background-clip:text; 
    -webkit-text-fill-color:transparent;
    font-size:120px;
    font-weight:900;
}

.metric{
    font-size:46px;
    font-family:Orbitron;
    font-weight:900;
}

.glow-card{
    background: linear-gradient(145deg, rgba(6,182,212,0.08), rgba(139,92,246,0.08));
    border:1px solid rgba(255,255,255,0.08);
    border-radius:15px;
    padding:12px;
    margin-bottom:10px;
    transition:0.4s;
}

.glow-card:hover{
    transform:translateY(-4px);
    box-shadow: 0px 0px 18px rgba(236,72,153,0.18);
}

div[data-testid="stSlider"], div[data-testid="stNumberInput"] {
    margin-bottom: -5px !important;
    padding: 2px 0px !important;
}

.stSlider{
    background:rgba(255,255,255,0.04);
    padding:8px 12px;
    border-radius:12px;
    border:1px solid rgba(255,255,255,0.05);
}

.stButton>button{
    width:100%;
    border:none;
    border-radius:18px;
    padding:20px;
    font-size:22px;
    font-weight:800;
    color:white;
    background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899);
    transition:0.4s;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow: 0px 0px 30px rgba(236,72,153,0.22);
}

.section-title{
    font-size:36px;
    font-weight:900;
    margin-top:80px;
    margin-bottom:25px;
    font-family: Orbitron;
    border-left: 5px solid #06b6d4;
    padding-left: 12px;
}

.column-header-1 {
    color: #22d3ee;
    font-weight: 800;
    font-size: 22px;
    margin-bottom: 10px;
}

.column-header-2 {
    color: #f472b6;
    font-weight: 800;
    font-size: 22px;
    margin-bottom: 10px;
}

@keyframes bgMove{
    0%{ background-position:0% 50%; }
    50%{ background-position:100% 50%; }
    100%{ background-position:0% 50%; }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

left, right = st.columns([1.6, 1])

with left:
    st.markdown("""
    <div class='hero-title'>
    NovaMind AI 🚀
    </div>
    <div class='hero-sub'>
    Futuristic AI platform for startup success prediction using Random Forest Machine Learning and investor intelligence analytics.
    </div>
    """, unsafe_allow_html=True)

with right:
    if lottie_ai:
        st_lottie(lottie_ai, height=300, key="ai")

# =========================================================
# AI MOOD ENGINE
# =========================================================

startup_moods = [
    "🦄 Unicorn Potential Detected",
    "🚀 Silicon Valley Energy Activated",
    "💸 Investors Are Watching This Startup",
    "🔥 Startup Has Viral Growth Signals",
    "🤖 AI Thinks This Could Be The Next Big Thing",
    "📈 Market Expansion Probability Increasing",
    "👀 Venture Capital Interest Detected"
]

st.markdown(f"""
<div style='background:linear-gradient(90deg, rgba(6,182,212,0.18), rgba(236,72,153,0.18));' class='result-display-card'>
{np.random.choice(startup_moods)}
</div>
""", unsafe_allow_html=True)

# =========================================================
# DASHBOARD CARDS
# =========================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class='glass'>
    <h2>🚀 Startups</h2>
    <div class='metric'>15K+</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='glass'>
    <h2>💰 Investments</h2>
    <div class='metric'>₹2,400 Cr</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='glass'>
    <h2>📈 Growth</h2>
    <div class='metric'>98%</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class='glass'>
    <h2>🌍 Countries</h2>
    <div class='metric'>42</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# INITIAL STAGE: INPUT SECTIONS
# =========================================================

st.markdown("""
<div class='section-title'>
🚀 Startup Intelligence Panel
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

# --- LEFT COLUMN: Growth & Innovation ---
with col_left:
    st.markdown("<div class='column-header-1'>📊 Growth & Innovation</div>", unsafe_allow_html=True)
    
    Growth_Rate = st.slider("📈 Growth Rate (%)", 0.0, 100.0, 60.0)
    Patent_Count = st.slider("📜 Patent Count", 0, 100, 15)
    Customer_Growth = st.slider("👥 Customer Growth (%)", 0.0, 100.0, 65.0)
    
    Company_Valuation = st.number_input("💎 Company Valuation (Lakh ₹)", min_value=0.0, value=2500.0, step=100.0)
    RD_Spend = st.number_input("🔬 R&D Spend (Lakh ₹)", min_value=0.0, value=1500.0, step=50.0)
    Funding_Amount = st.number_input("🏦 Funding Amount (Lakh ₹)", min_value=0.0, value=4000.0, step=100.0)

# --- RIGHT COLUMN: People & Market ---
with col_right:
    st.markdown("<div class='column-header-2'>👥 People & Market</div>", unsafe_allow_html=True)
    
    Customer_Satisfaction = st.slider("⭐ Customer Satisfaction", 0.0, 10.0, 8.0)
    Employee_Retention_Rate = st.slider("👨‍💻 Employee Retention (%)", 0.0, 100.0, 78.0)
    Innovation_Score = st.slider("🧠 Innovation Score", 0.0, 10.0, 8.5)
    Founder_Experience = st.slider("👨‍💼 Founder Experience (Years)", 0.0, 30.0, 10.0)
    Market_Competition = st.slider("⚔️ Market Competition", 0.0, 10.0, 4.0)
    
    Revenue = st.number_input("💵 Revenue (Lakh ₹)", min_value=0.0, value=3000.0, step=100.0)

# DYNAMIC 3-YEAR VALUATION EXPANDER
with st.expander("🔮 Optional: View Dynamic 3-Year Valuation Run Rate Projections"):
    st.markdown("<p style='color: #cbd5e1;'>Simulated execution curve based on current runtime growth rates:</p>", unsafe_allow_html=True)
    sim_col1, sim_col2 = st.columns(2)
    with sim_col1:
        years = [1, 2, 3]
        projected_rev = [Revenue * ((1 + (Growth_Rate/100))**y) for y in years]
        projected_val = [Company_Valuation * ((1 + (Growth_Rate/120))**y) for y in years]
        
        sim_df = pd.DataFrame({
            "Year": ["Year 1", "Year 2", "Year 3"], 
            "Revenue (Lakh ₹)": projected_rev, 
            "Valuation (Lakh ₹)": projected_val
        })
        st.dataframe(sim_df.style.format({"Revenue (Lakh ₹)": "{:.2f}", "Valuation (Lakh ₹)": "{:.2f}"}))
    with sim_col2:
        fig_sim = px.line(sim_df, x="Year", y=["Revenue (Lakh ₹)", "Valuation (Lakh ₹)"], markers=True, title="Growth Path Matrix Vector")
        fig_sim.update_layout(
            template='plotly_dark', 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_sim, use_container_width=True)

# =========================================================
# PROCESS VARIABLE PACKAGING
# =========================================================
input_data = np.array([[
    Funding_Amount, Growth_Rate, Revenue, RD_Spend,
    Innovation_Score, Market_Competition, Customer_Growth,
    Founder_Experience, Customer_Satisfaction, Company_Valuation,
    Employee_Retention_Rate, Patent_Count
]])

st.write("")

# Action validation processing trigger
if st.button("🚀 Run Evaluation Engine Diagnostics"):
    st.session_state.diagnostics_run = True

# =========================================================
# REVEAL PANEL STAGE: ONLY TRIGGERS UPON BUTTON PRESS
# =========================================================
if st.session_state.diagnostics_run:
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.1); margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🧠 AI Diagnostics Engine Output</div>", unsafe_allow_html=True)

    with st.spinner("🧠 AI analyzing startup ecosystem..."):
        time.sleep(1.2)

    if model is not None:
        prediction = model.predict(input_data)[0]
    else:
        if Innovation_Score > 7.5 and Growth_Rate > 50:
            prediction = 2
        elif Innovation_Score > 5.0 or Growth_Rate > 30:
            prediction = 1
        else:
            prediction = 0

    if prediction == 0:
        status = "Failed"
        score = 35
        insight = "Weak growth and financial signals detected."
    elif prediction == 1:
        status = "Moderate"
        score = 68
        insight = "Startup has moderate scalability potential."
    else:
        status = "Successful"
        score = 92
        insight = "Strong innovation and market expansion detected."
        st.balloons()

    st.markdown(f"""
    <div class='glass' style='margin-top:20px;text-align:center;'>
        <h1>🚀 Startup Status</h1>
        <h1 style='font-size:85px; font-weight:900; font-family:Orbitron;'>{status}</h1>
        <h2>AI Startup Success Score</h2>
        <h1 class='result-percentage-text'>{score}%</h1>
        <p style='font-size:20px;color:#cbd5e1;'>{insight}</p>
    </div>
    """, unsafe_allow_html=True)

    # Investor Sentiment Response
    if score > 85:
        investor = "🤑 Top investors are fighting to fund this startup."
    elif score > 60:
        investor = "🤝 Investors see moderate scalability potential."
    else:
        investor = "😬 Investors think this startup needs major improvements."

    st.markdown(f"""
    <div class='glass' style='margin-top:25px;'>
        <h2>🎯 Investor Reaction</h2>
        <h3 style='color:#dbeafe;'>{investor}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Multi-Variate Analytics Visual Graphs
    st.write("")
    ch1, ch2 = st.columns(2)

    with ch1:
        analytics = pd.DataFrame({
            'Feature': ['Funding', 'Growth', 'Innovation', 'Revenue', 'Customers'],
            'Value': [Funding_Amount/100, Growth_Rate, Innovation_Score*10, Revenue/100, Customer_Growth]
        })

        fig = px.bar(analytics, x='Feature', y='Value', color='Value', title='📊 Startup Analytics')
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with ch2:
        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(
            r=[Innovation_Score, Growth_Rate/10, Customer_Growth/10, Employee_Retention_Rate/10, Customer_Satisfaction],
            theta=['Innovation', 'Growth', 'Customers', 'Retention', 'Satisfaction'],
            fill='toself'
        ))
        radar.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            polar=dict(radialaxis=dict(visible=True, range=[0, 10]))
        )
        st.plotly_chart(radar, use_container_width=True)

    # AI Optimization Guidelines
    st.markdown("### 🤖 AI Strategic Recommendations")
    recs = []
    if Funding_Amount < 2000:
        recs.append("💰 Increase investor partnerships and fundraising.")
    if Innovation_Score < 6:
        recs.append("🧠 Focus on innovation and patents.")
    if Customer_Growth < 50:
        recs.append("📈 Improve marketing and customer acquisition.")
    if Revenue < 2000:
        recs.append("💵 Improve monetization strategy.")
    if len(recs) == 0:
        recs.append("🚀 Excellent startup ecosystem detected.")

    for r in recs:
        st.markdown(f"<div class='glow-card'><h3>{r}</h3></div>", unsafe_allow_html=True)

    # File Download Endpoint Structure
    st.write("")
    st.download_button(
        label="📥 DOWNLOAD EXECUTIVE DIAGNOSTIC DATA (CSV)",
        data=analytics.to_csv(index=False),
        file_name="startup_diagnostic_report.csv",
        mime="text/csv"
    )

    # =========================================================
    # UPGRADED HIGHLY MOTIVATIONAL VERDICT SYSTEM
    # =========================================================
    if score > 90:
        verdict = "🚀 This startup is giving serious fantastic vibes. Keep pushing, the market is yours to dominate!"
    elif score > 75:
        verdict = "🔥 Incredible execution markers! Your fundamentals are exceptionally crisp. Investors are circling."
    elif score > 55:
        verdict = "⚡ Great foundation established! With micro-adjustments to market positioning, scalability is right on the horizon."
    else:
        verdict = "🏁 Grit defines the winner. Every massive breakthrough begins as a turnaround script. Iterate, refine, and break barriers!"

    st.markdown(f"""
    <div style='margin-top:25px; padding:25px; border-radius:20px; background:linear-gradient(90deg, rgba(6,182,212,0.15), rgba(236,72,153,0.15)); border:1px solid rgba(255,255,255,0.1); text-align:center; font-size:28px; font-weight:800;'>
    {verdict}
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<hr>
<center>
<h4 style='color:#94a3b8;'>
NovaMind AI • Startup Intelligence Platform • Random Forest Machine Learning
</h4>
</center>
""", unsafe_allow_html=True)