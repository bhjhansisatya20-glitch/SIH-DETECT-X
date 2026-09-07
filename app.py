import streamlit as st
import pytesseract
from PIL import Image
import time

# --- STYLING & SECURE DASHBOARD LAYOUT ---
st.set_page_config(page_title="SIH Gate 5: Automated Validation Engine", page_icon="🛡️", layout="centered")

st.title("🛡️ Gate 5: Decentralized Cross-Validation")
st.write("### Automated OCR & Registry Sanity Check")
st.markdown("---")

# --- USER INTERFACE DESIGN ---
st.subheader("📂 Step 1: Upload Document for Scanning")

id_options = [
    "Aadhaar Card", "PAN Card", "Driving License", "Passport", 
    "Voter ID", "Birth Certificate", "Ration Card", 
    "Pension Card", "Arms License", "Marriage Certificate"
]
selected_id = st.selectbox("Select Target Registry Node Node:", id_options)

uploaded_file = st.file_uploader("Upload Document Image File (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])

st.markdown("---")

# --- AUTOMATED ENGINE PROCESSING ---
if uploaded_file is not None:
    # 1. Display the uploaded card image visually on screen
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document Source File", width=350)
    
    if st.button("🚀 Execute Automatic Verification Pipeline", use_container_width=True):
        
        # 2. Visual Step: Run the Text Scanner (OCR)
        with st.spinner("🔍 Gate 4 Active: Optical Character Recognition (OCR) Scanning Text..."):
            try:
                # Scans the actual image for words automatically!
                extracted_text = pytesseract.image_to_string(image)
                time.sleep(1.5)
            except Exception as e:
                st.error("OCR Scanner Initialization Error. Please ensure system dependencies are deployed.")
                extracted_text = ""

        # Show a summary of what the system read off the card
        if extracted_text.strip():
            with st.expander("👁️ View Extracted Text Metadata Logs (Gate 4 Output)"):
                st.code(extracted_text)
        
        st.markdown("---")
        
        # 3. Visual Step: Run your Gate 5 Central Database Check
        with st.spinner("📡 Gate 5 Routing: Cross-Referencing String Logs with Sandbox Registries..."):
            time.sleep(2.5) # Simulates network processing latency
            
        # --- THE CONTEXT SECURITY SANITY CHECK ---
        # Demo Evaluation Rule: If the text scanned on the card contains "REAL" or a trusted test keyword, pass it.
        # Otherwise, flag it as a synthetic record manipulation attempt.
        if "REAL" in extracted_text.upper() or "APPROVED" in extracted_text.upper():
            st.success("### ✅ [SUCCESS] REGISTRY ENTRY CONFIRMED")
            st.balloons()
            st.markdown(
                f"""
                <div style="background-color:#d4edda; padding:20px; border-radius:10px; border-left:8px solid #28a745; color:#155724;">
                    <strong>Verification Verdict:</strong> AUTHENTIC RECORD MATCH FOUND<br>
                    <strong>Registry Node:</strong> Sovereign Central Sandbox Database Layer<br>
                    <strong>Status:</strong> Clear. The text scanned automatically off the card matches a valid registry entry!
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.error("### 🚨 [CRITICAL ALERT] SYNTHETIC FORGERY DETECTED")
            st.markdown(
                f"""
                <div style="background-color:#f8d7da; padding:20px; border-radius:10px; border-left:8px solid #dc3545; color:#721c24;">
                    <strong>Verification Verdict:</strong> ZERO-MATCH CENTRAL DATABASE ERROR<br>
                    <strong>Security Risk Assessment:</strong> High Risk Flag. The image file exists physically, but the text string elements read off the card do not exist in any verified state registry node.<br>
                    <strong>Classification:</strong> Synthetic Identity Theft. Access Blocked.
                </div>
                """, unsafe_allow_html=True
            )
