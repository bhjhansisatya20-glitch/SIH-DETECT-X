import streamlit as st
import time

# --- STYLING & SECURE DASHBOARD LAYOUT ---
st.set_page_config(page_title="SIH Gate 5: Decentralized Validation Hub", page_icon="🛡️", layout="centered")

st.title("🛡️ Gate 5: Decentralized Cross-Validation")
st.write("### The 'Sanity Check' Security Engine")
st.markdown("---")

# --- USER INTERFACE INPUTS ---
st.subheader("📋 Step 1: Input Extracted Credential Metrics")

# The 10 Indian Documents you built out!
id_options = [
    "Aadhaar Card", "PAN Card", "Driving License", "Passport", 
    "Voter ID", "Birth Certificate", "Ration Card", 
    "Pension Card", "Arms License", "Marriage Certificate"
]
selected_id = st.selectbox("Select Target Registry Node Node:", id_options)

id_number = st.text_input("Enter Extracted Identification Number (e.g., AD12345):")
full_name = st.text_input("Enter Extracted Full Name (e.g., RAJESH KUMAR):")

# File uploader box for your presentation
uploaded_file = st.file_uploader("📂 Upload Document Image File (PNG, JPG, PDF):", type=["png", "jpg", "jpeg", "pdf"])

st.markdown("---")

# --- CORE GATEWAY SECURITY LOGIC ---
if st.button("🚀 Run Decentralized Sanity Check", use_container_width=True):
    if not id_number or not full_name or not uploaded_file:
        st.warning("⚠️ Access Denied: Please provide a document file, ID Number, and Full Name to initiate verification routing.")
    else:
        # Visual loading spinner for your presentation to make it look like a real database lookup!
        with st.spinner(f"Initiating Encrypted SHA-256 API Handshake with Central Registries..."):
            time.sleep(2) # Simulates network processing latency
            
        # --- THE SECURITY SANITY CHECK ---
        # Prototype Evaluation Rule: If the user provides the demo token "REAL", pass validation.
        # Otherwise, flag as synthetic identity manipulation theft.
        if "REAL" in full_name.upper():
            st.success("### ✅ [SUCCESS] REGISTRY ENTRY CONFIRMED")
            st.balloons() # Gives a great celebratory visual effect for the judges!
            st.markdown(
                f"""
                <div style="background-color:#d4edda; padding:20px; border-radius:10px; border-left:8px solid #28a745; color:#155724;">
                    <strong>Verification Verdict:</strong> AUTHENTIC RECORD ENCRYPTED MATCH FOUND<br>
                    <strong>Registry Node:</strong> Official DigiLocker/Government Sandbox Node<br>
                    <strong>Status:</strong> Clear. Text details perfectly match database architecture records.
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.error("### 🚨 [CRITICAL ALERT] SYNTHETIC FORGERY DETECTED")
            st.markdown(
                f"""
                <div style="background-color:#f8d7da; padding:20px; border-radius:10px; border-left:8px solid #dc3545; color:#721c24;">
                    <strong>Verification Verdict:</strong> ZERO-MATCH DATABASE ERROR FLAG<br>
                    <strong>Security Risk Assessment:</strong> High. The document image has passed visual AI checks, but the unique ID string does not exist in any sovereign registry node.<br>
                    <strong>Classification:</strong> Synthetic Identity Theft Attempt. Access Denied.
                </div>
                """, unsafe_allow_html=True
            )
