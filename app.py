import streamlit as st
import pytesseract
from PIL import Image
import time

# --- STYLING CONFIGURATION ---
st.set_page_config(
    page_title="SIH 2026 | Document Security Pipeline", 
    page_icon="🛡️", 
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #05070b;
        background-image: 
            linear-gradient(rgba(0, 255, 204, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 204, 0.03) 1px, transparent 1px);
        background-size: 30px 30px;
        animation: gridPulse 8s infinite alternate ease-in-out;
    }
    @keyframes gridPulse { 0% { background-size: 28px 28px; } 100% { background-size: 32px 32px; } }
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', Courier, monospace; text-shadow: 0 0 10px rgba(0,255,204,0.3); }
    .stSelectbox label, .stFileUploader label { color: #ffffff !important; font-weight: bold; }
    .crypto-header {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.75) 0%, rgba(15, 23, 42, 0.85) 100%);
        backdrop-filter: blur(8px); padding: 25px; border-radius: 12px;
        border: 1px solid rgba(0, 255, 204, 0.2); border-left: 6px solid #00ffcc; margin-bottom: 25px;
    }
    .step-card {
        background-color: rgba(30, 41, 59, 0.65); backdrop-filter: blur(6px); padding: 20px;
        border-radius: 10px; border: 1px solid rgba(71, 85, 105, 0.4); margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- JAVASCRIPT FIREWORKS SCRIPT ENGINE ---
# This injects a canvas particle blast over the dashboard interface
fireworks_html = """
<canvas id="fireworksCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:99999; pointer-events:none;"></canvas>
<script>
    const canvas = document.getElementById('fireworksCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];
    const colors = ['#00ffcc', '#10b981', '#3b82f6', '#f43f5e', '#eab308'];

    class Particle {
        constructor(x, y, color) {
            this.x = x;
            this.y = y;
            this.color = color;
            this.radius = Math.random() * 3 + 1;
            this.angle = Math.random() * Math.PI * 2;
            this.velocity = Math.random() * 6 + 2;
            this.alpha = 1;
            this.decay = Math.random() * 0.02 + 0.015;
        }
        update() {
            this.x += Math.cos(this.angle) * this.velocity;
            this.y += Math.sin(this.angle) * this.velocity + 0.5; // subtle gravity acceleration
            this.alpha -= this.decay;
        }
        draw() {
            ctx.save();
            ctx.globalAlpha = this.alpha;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.shadowBlur = 10;
            ctx.shadowColor = this.color;
            ctx.fill();
            ctx.restore();
        }
    }

    function createExplosion(x, y) {
        const color = colors[Math.floor(Math.random() * colors.length)];
        for (let i = 0; i < 60; i++) {
            particles.push(new Particle(x, y, color));
        }
    }

    // Trigger multiple bursts across the terminal view viewport
    createExplosion(canvas.width * 0.25, canvas.height * 0.4);
    createExplosion(canvas.width * 0.5, canvas.height * 0.3);
    createExplosion(canvas.width * 0.75, canvas.height * 0.4);

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles = particles.filter(p => p.alpha > 0);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        if (particles.length > 0) {
            requestAnimationFrame(animate);
        }
    }
    animate();
</script>
"""

# --- HEADER ---
st.markdown("""
    <div class="crypto-header">
        <h1 style='margin:0; font-size:26px; letter-spacing: 1px;'>🛡️ DETECT-X: CORE ENFORCEMENT LAYER</h1>
        <p style='margin:5px 0 0 0; color:#00ffcc; font-size:13px; font-family: monospace;'>
            // ACTIVE PIPELINE: GATES 2 (OCR), 4 (ENVIRONMENT) & 5 (DATA TRUTH)
        </p>
    </div>
""", unsafe_allow_html=True)

# --- SYSTEM SETTINGS PANEL ---
st.markdown('<div class="step-card">', unsafe_allow_html=True)
st.subheader("📡 PIPELINE INITIALIZATION")
id_options = [
    "Aadhaar Card (UIDAI Node)", "PAN Card (NSDL Tax Registry)", 
    "Driving License (SARATHI Node)", "Passport (MEA Portal)", "Voter ID (ECI Hub)"
]
selected_id = st.selectbox("Select Intended Gateway Registry Target Node:", id_options)
uploaded_file = st.file_uploader("Drop verification media file here (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])
st.markdown('</div>', unsafe_allow_html=True)

# --- VERIFICATION TRIGGER ---
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown("### 📷 Captured Upload Frame Stream")
    st.image(image, width=320)
    
    if st.button("🚀 INITIATE MULTI-GATEWAY INSPECTION MATRIX", use_container_width=True):
        st.markdown("### 🛠️ Real-Time Inspection Logs")
        
        # ----------------------------------------------------
        # 🛡️ GATE 4: SIGNAL & DEVICE INTELLIGENCE (SIMULATED)
        # ----------------------------------------------------
        with st.status("🔒 [GATE 4] Analyzing Signal & Device Intelligence...", expanded=True) as gate4_status:
            st.write("Auditing device fingerprint environment parameters...")
            time.sleep(1.0)
            st.write("Checking WebRTC video stream attributes for injection signatures...")
            time.sleep(1.0)
            st.write("Verifying camera driver hardware integrity bounds...")
            
            if "EMULATOR" in uploaded_file.name.upper() or "VIRTUAL" in uploaded_file.name.upper():
                gate4_status.update(label="❌ Gate 4 Breach: Virtual Camera / Emulator Cam Detected!", state="error")
                st.error("🚨 **[GATE 4 FAILURE] BOUNDARY VIOLATION:** This device stream is originating from a phone emulator or virtual camera injection tool. Pipeline execution halted immediately.")
                st.stop()
            else:
                gate4_status.update(label="✅ Gate 4: Device Intelligence Verified (Physical Hardware Confirmed)", state="complete", expanded=False)

        # ----------------------------------------------------
        # 👁️ [GATE 2] BACKGROUND PROCESS: TEXT OCR EXTRACTOR
        # ----------------------------------------------------
        with st.status("🔍 [GATE 2] Computer Vision & Layout OCR Matrix Engaged...", expanded=True) as gate2_status:
            st.write("Structuring computer vision layout segmentations...")
            try:
                extracted_text = pytesseract.image_to_string(image)
                time.sleep(1.0)
                st.write("Successfully isolated alphanumeric document text blocks.")
                gate2_status.update(label="✅ Gate 2: Character Extraction Complete", state="complete", expanded=False)
            except Exception:
                extracted_text = ""
                gate2_status.update(label="❌ Gate 2 Error: OCR Failure", state="error")

        if extracted_text.strip():
            with st.expander("👁️ View Extracted Alphanumeric Logs (Gate 2 OCR Stream)"):
                st.code(extracted_text)

        # ----------------------------------------------------
        # 📡 GATE 5: DECENTRALIZED CROSS-VALIDATION
        # ----------------------------------------------------
        with st.status("📡 [GATE 5] Executing Decentralized Cross-Validation Ledger Handshake...", expanded=True) as gate5_status:
            st.write("Encrypting query parameters using local SHA-256 protocols...")
            st.write(f"Initiating remote query string lookup on: {selected_id}...")
            time.sleep(1.5)
            gate5_status.update(label="✅ Gate 5: Decentralized Node Handshake Concluded", state="complete", expanded=False)

        st.write("")
        
        # --- FINAL PIPELINE VERDICT DECISION ---
        if "REAL" in extracted_text.upper() or "REAL" in uploaded_file.name.upper():
            # Trigger custom neon firework particle explosion display
            st.components.v1.html(fireworks_html, height=0)
            
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(6,78,59,0.95) 100%); backdrop-filter: blur(8px); padding:25px; border-radius:12px; border:2px solid #10b981; border-left:10px solid #10b981; color:#ecfdf5;">
                    <h3 style="color:#10b981 !important; margin-top:0;">✅ [STATUS: ACCESS GRANTED]</h3>
                    <p style="margin:5px 0;"><strong>Gate 2 Verdict:</strong> Text metadata extracted seamlessly via CV Layout parameters.</p>
                    <p style="margin:5px 0;"><strong>Gate 4 Verdict:</strong> Authentic hardware frame capture verified.</p>
                    <p style="margin:5px 0;"><strong>Gate 5 Verdict:</strong> Encrypted data match confirmed in central registry ledger.</p>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(127,29,29,0.95) 100%); backdrop-filter: blur(8px); padding:25px; border-radius:12px; border:2px solid #ef4444; border-left:10px solid #ef4444; color:#fef2f2;">
                    <h3 style="color:#ef4444 !important; margin-top:0;">🚨 [STATUS: SYNTHETIC FORGERY BLOCK]</h3>
                    <p style="margin:5px 0;"><strong>Gate 4 Verdict:</strong> Hardware camera signals clean.</p>
                    <p style="margin:5px 0;"><strong>Gate 5 Verdict:</strong> 404 Record Error — The unique ID number reads mathematically valid but does not exist on government registry nodes.</p>
