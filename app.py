import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Custom CSS for full-width layout and enhancements
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');

/* Full-width layout modifications */
.main > div, .main > div > div {
    max-width: 100% !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

.st-emotion-cache-1y4p8pa {
    padding: 2rem 1rem !important;
}

/* Unified component styling */
.stButton>button, .prediction-box, .class-info {
    transition: all 0.3s ease-in-out;
}

.prediction-box {
    background: rgba(0, 0, 0, 0.7);
    border-radius: 20px;
    border: 2px solid #9D4EDD;
    box-shadow: 0 0 30px #C77DFF;
    margin: 1rem 0;
}

/* Footer styling */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(43, 9, 71, 0.9);
    padding: 1rem 2rem;
    text-align: center;
    border-top: 1px solid #9D4EDD;
    z-index: 1000;
}

/* Responsive columns */
@media (max-width: 768px) {
    .main > div {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    .st-emotion-cache-1y4p8pa {
        padding: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# Add sidebar with logo
with st.sidebar:
    st.image('logo.png', use_container_width=True, output_format='PNG', caption='Stellar Classifier Pro')
    st.markdown("---")
    st.markdown("### About")
    st.markdown("Classify stars into 3 cosmic categories based on spectral characteristics")

# Spectral Class Configuration
SPECTRAL_MAPPING = {0: 'Blue Giants', 1: 'Solar Analogs', 2: 'Cool Dwarfs'}
SPECTRAL_INFO = {
    'Blue Giants': {
        'color': '#4A90E2', 'temp_range': "10,000-40,000K",
        'desc': "Massive hot stars (10,000-40,000K)\n• Young stellar objects\n• Extreme UV radiation\n• Short-lived cosmic powerhouses",
        'examples': "O-type, B-type stars"
    },
    'Solar Analogs': {
        'color': '#FFD700', 'temp_range': "5,000-7,500K",
        'desc': "Sun-like stars (5,000-7,500K)\n• Potential habitable zones\n• Stable energy output\n• Common in spiral arms",
        'examples': "F-type, G-type stars"
    },
    'Cool Dwarfs': {
        'color': '#FF6B6B', 'temp_range': "2,400-5,000K",
        'desc': "Low-mass cool stars (2,400-5,000K)\n• Long-lived cosmic survivors\n• Most abundant stellar type\n• Red/orange spectral signature",
        'examples': "K-type, M-type stars"
    }
}

@st.cache_resource
def load_model():
    return (
        joblib.load('star_classification_model.pkl'),
        joblib.load('star_scaler.pkl')
    )

def main():
    st.title("🌌 Cosmic Classifier Dashboard")
    model, scaler = load_model()

    # Full-width dashboard layout
    with st.container():
        col1, col2, col3 = st.columns([2, 3, 2])

        with col1:
            with st.container():
                st.subheader("⚙️ Stellar Parameters")
                temp = st.slider("Temperature (K)", 1939, 40000, 5776)
                lum = st.slider("Luminosity (L/L☉)", 0.00008, 849420.0, 0.0705)
                rad = st.slider("Radius (R/R☉)", 0.0084, 1948.5, 0.7625)
                abs_mag = st.slider("Abs Magnitude (Mv)", -11.92, 20.06, 8.313)

            if st.button("🚀 Analyze Stellar Profile", use_container_width=True):
                # Create input dataframe with correct column order
                input_data = pd.DataFrame([[temp, lum, rad, abs_mag]], 
                    columns=['Temperature (K)', 'Luminosity (L/Lo)', 
                            'Radius (R/Ro)', 'Absolute magnitude (Mv)'])
                
                # Scale features using the loaded scaler
                scaled_data = scaler.transform(input_data)
                
                # Get prediction and map to class name
                prediction = model.predict(scaled_data)[0]
                st.session_state.prediction = SPECTRAL_MAPPING[prediction]

        with col2:
            st.subheader("🔭 Prediction Results")
            if 'prediction' in st.session_state:
                info = SPECTRAL_INFO[st.session_state.prediction]
                st.markdown(f"""
                <div class='prediction-box'>
                    <h2 style='color: {info['color']}; text-align: center'>
                    🌟 {st.session_state.prediction}</h2>
                    <div style='text-align: center; margin: 2rem 0'>
                        <div style='background: {info['color']}; 
                            width: 100px; height: 100px; margin: 0 auto;
                            border-radius: 50%; box-shadow: 0 0 30px {info['color']};'>
                        </div>
                    </div>
                    <p style='font-size: 1.1rem; text-align: center'>{info['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

        with col3:
            st.subheader("📚 Star Classes")
            for class_name, info in SPECTRAL_INFO.items():
                st.markdown(f"""
                <div class='class-info' style='border-left: 5px solid {info['color']}; margin-bottom: 1rem'>
                    <h4 style='color: {info['color']}'>{class_name}</h4>
                    <p><strong>Temperature:</strong> {info['temp_range']}</p>
                    <p><strong>Examples:</strong> {info['examples']}</p>
                </div>
                """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class='footer'>
        <span style='color: #9D4EDD'>Cosmic Classifier Pro with astro_salma</span> • 
        © 2025 Stellar Analytics • 
        v2.1.0
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()