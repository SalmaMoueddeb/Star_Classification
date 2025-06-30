# 🌠 Stars Classification
This project focuses on classifying stars based on their physical and spectral features. Using a dataset containing various astronomical attributes, we train an XGBoost classifier to predict the type of star, and build an interactive web application using Streamlit for easy use and visualization.

# 📊 Dataset Overview
The dataset includes several features describing the characteristics of stars:

**Temperature** (K) — Absolute surface temperature

**Luminosity** (L/Lo) — Relative luminosity (Lo = 3.828 × 10²⁶ Watts, average solar luminosity)

**Radius** (R/Ro) — Relative radius (Ro = 6.9551 × 10⁸ m, average solar radius)

**Absolute Magnitude** (Mv)

**Star Color** (e.g., White, Red, Blue, Yellow, Yellow-Orange)

**Spectral Class** (O, B, A, F, G, K, M)

**Star Type (Target):**

Red Dwarf

Brown Dwarf

White Dwarf

Main Sequence

Supergiants

Hypergiants

# 🤖 Model
We use XGBoost, a powerful gradient boosting algorithm, for the classification task. It was chosen for its efficiency and strong performance on structured/tabular data.

# 🚀 App Functionality
The web app, built with Streamlit, allows users to:

Input the properties of a star (e.g., temperature, luminosity, radius, color, spectral class)

Get an instant prediction of the star type

Visualize where the star falls within known categories

# 🛠️ How to Run the Project
### 1. Clone the repository git 
<pre> clone https://github.com/SalmaMoueddeb/Star_Classification.git cd star-classification </pre>
### 2. (Optional but recommended) Create and activate a virtual environment
### For Windows python
<pre> -m venv venv venv\Scripts\activate </pre>
### For macOS/Linux 
<pre> python3 -m venv venv source venv/bin/activate </pre>
### 3. Run the Streamlit app 
<pre> streamlit run app.py</pre>

