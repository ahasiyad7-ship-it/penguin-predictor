import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Penguin Predictor", layout="centered")
st.title("Penguin Species Predictor - 5 Species")
st.write("Enter the penguin body measurements to predict its species with photo.")

# Professional Photo Style - No White Sides, Full Photo
st.markdown("""
<style>
img {
    width: 100% !important;
    height: auto !important;
    object-fit: cover !important;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Load Real Dataset - Contains 3 Species: Adelie, Chinstrap, Gentoo
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
df = pd.read_csv(url).dropna()
df = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']]

# Add 2 More Species - Emperor and King (Based On Real Measurement Ranges)
np.random.seed(42)

# Emperor Penguin - The Largest Penguin
emperor = pd.DataFrame({
    'bill_length_mm': np.random.uniform(50, 60, 100),
    'bill_depth_mm': np.random.uniform(20, 25, 100),
    'flipper_length_mm': np.random.uniform(350, 400, 100),
    'body_mass_g': np.random.uniform(22000, 40000, 100),
    'species': 'Emperor'
})

# King Penguin - The Second Largest Penguin
king = pd.DataFrame({
    'bill_length_mm': np.random.uniform(45, 55, 100),
    'bill_depth_mm': np.random.uniform(18, 22, 100),
    'flipper_length_mm': np.random.uniform(300, 350, 100),
    'body_mass_g': np.random.uniform(11000, 16000, 100),
    'species': 'King'
})

# Combine All 5 Species Into One Dataset
df = pd.concat([df, emperor, king])

# Train Machine Learning Model
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

model = RandomForestClassifier()
model.fit(X, y)

# Penguin Images - 5 Clear HD Photos, Correct Species
penguin_images = {
    "Adelie": "https://commons.wikimedia.org/wiki/Special:FilePath/Hope_Bay-2016-Trinity_Peninsula–Adélie_penguin_(Pygoscelis_adeliae)_04.jpg?width=1000",
    "Chinstrap": "https://commons.wikimedia.org/wiki/Special:FilePath/A_chinstrap_penguin_(Pygoscelis_antarcticus)_on_Deception_Island_in_Antarctica.jpg?width=1000",
    "Gentoo": "https://commons.wikimedia.org/wiki/Special:FilePath/Brown_Bluff-2016-Tabarin_Peninsula–Gentoo_penguin_(Pygoscelis_papua)_03.jpg?width=1000",
    "Emperor": "https://commons.wikimedia.org/wiki/Special:FilePath/Emperor_penguin_(Aptenodytes_forsteri).jpg?width=1000",
    "King": "https://commons.wikimedia.org/wiki/Special:FilePath/King_Penguin_(Aptenodytes_patagonicus).jpg?width=1000"
}

# Penguin Information For Each Species
penguin_info = {
    "Adelie": "Small penguin with a white ring around its eyes.",
    "Chinstrap": "Penguin with a black strap under its chin.",
    "Gentoo": "Penguin with a white patch on its head and a long tail. It is the fastest swimmer.",
    "Emperor": "Largest penguin in the world. Lives in Antarctica, up to 40kg weight.",
    "King": "Second largest penguin. Has bright orange colour on neck and chest."
}

# Get Measurements From User - Expanded Range For Large Penguins
st.subheader("Enter Penguin Measurements:")

bill_length = st.slider("Bill Length (mm)", 30.0, 65.0, 40.0)
bill_depth = st.slider("Bill Depth (mm)", 13.0, 26.0, 18.0)
flipper_length = st.slider("Flipper Length (mm)", 170.0, 400.0, 190.0)
body_mass = st.slider("Body Mass (g)", 2700.0, 40000.0, 3800.0)

# Predict And Display Result With Photo
if st.button("Predict Penguin Type"):
    result = model.predict([[bill_length, bill_depth, flipper_length, body_mass]])[0]

    st.success(f"Predicted Species is: {result}")
    st.write(penguin_info[result])

    # Display Photo In The Center
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        st.image(penguin_images[result], caption=f"This is a {result} Penguin", use_container_width=True)