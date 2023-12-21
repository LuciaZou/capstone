import streamlit as st
import pandas as pd
import numpy as np
import joblib
# import xgboost
xgboost_model = joblib.load("xgbF.pkl")

st.title("Lucia's Streamlit Page")

# Read the contents of the README file
with open('ReadMe.md', 'r', encoding='utf-8') as file:
    readme_text = file.read()

# Display the contents in the sidebar
st.sidebar.title("About")
st.sidebar.markdown(readme_text)

# Now let's add the QR code to the sidebar below the README content
qr_code_image = 'image_6483441.JPG'
st.sidebar.image(qr_code_image, caption='Scan the QR Code')

st.markdown(
    """
    <style>
    .main {
        background: url("https://getwallpapers.com/wallpaper/full/0/6/b/1418311-gradient-wallpapers-1920x1200-mobile.jpg");
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        text-color: white;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

# Text
st.write("This is a simple Streamlit app for making predictions!")

st.image('d60309127f7dd4dd05ec3e21e4b5673c.jpg', width=250)

# Custom CSS to inject into the Streamlit app
st.markdown("""
<style>
label {
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

# Create inputs for numerical feature
week = st.number_input('Week',step = 1,min_value = 1, max_value = 52)
county_number=st.number_input('county_number',step = 1,min_value = 1, max_value = 99)

pack_options = {
    'pack_1': 1, 'pack_2': 2, 'pack_3': 3, 'pack_4': 4,
    'pack_5': 5, 'pack_6': 6, 'pack_8': 7, 'pack_9': 8, 'pack_10': 9,
    'pack_12': 10, 'pack_15': 11, 'pack_16': 12, 'pack_18': 13,
    'pack_20': 14, 'pack_24': 15, 'pack_28': 16, 'pack_30': 17,
    'pack_44': 18, 'pack_48': 19, 'pack_60': 20, 'pack_120': 21
}
pack = st.selectbox("Pack", list(pack_options.keys()))

# Encoding the selected pack
encoded_pack = pack_options[pack]

bottle_volume_options = {'bottle_volume_ml_20':1,
    'bottle_volume_ml_50': 2, 'bottle_volume_ml_100': 3, 'bottle_volume_ml_150': 6,
    'bottle_volume_ml_175': 4, 'bottle_volume_ml_200': 5, 'bottle_volume_ml_375': 25,
    'bottle_volume_ml_400': 7, 'bottle_volume_ml_600': 8, 'bottle_volume_ml_603': 9,
    'bottle_volume_ml_700': 10, 'bottle_volume_ml_750': 11, 'bottle_volume_ml_800': 12,
    'bottle_volume_ml_850': 13, 'bottle_volume_ml_900': 14, 'bottle_volume_ml_950': 15,
    'bottle_volume_ml_1000': 16, 'bottle_volume_ml_1200': 17, 'bottle_volume_ml_1750': 18,
    'bottle_volume_ml_1800': 19, 'bottle_volume_ml_2250': 20, 'bottle_volume_ml_2400': 21,
    'bottle_volume_ml_3500': 22, 'bottle_volume_ml_4500': 23, 'bottle_volume_ml_5250': 24
}
bottle_volume = st.selectbox("Bottle Volume (ml)", list(bottle_volume_options.keys()))
encoded_bottle_volume = bottle_volume_options[bottle_volume]

# Dropdown for Alcohol Type (assuming label encoding)
alcohol_type_options = {
    'Brandy': 50, 'Cocktail': 23, 'Specialty': 0, 
    'Vodka': 1, 'Whisky': 2, 'Cordials&Liqueur': 3, 'Spirits': 4, 'Tequila': 5, 
    'Bourbon': 6, 'Rum': 7, 'Schnapps': 8, 'Scotch': 9, 'Gin': 10,'OtherCategories':11
}

# The variable to hold the selected alcohol type from the dropdown
selected_alcohol_type = st.selectbox("Alcohol Type", list(alcohol_type_options.keys()))

# Markdown
st.markdown("""
    ### Volume
    - Volume_3 is the liquor has 100.01 to 200 L
    - Volume_4 is the liquor has 200.01 to 500 L
    - Volume_5 is the liquor has 500.01 to 1000 L
    - Volume_6 is the liquor has more than 1000.01 L
""")

# Assuming these are the volume options
volume_options = {
    "volume_3": "100.01 to 200 L",
    "volume_4": "200.01 to 500 L",
    "volume_5": "500.01 to 1000 L",
    "volume_6": "More than 1000.01 L"
}

# Using radio buttons for single selection
selected_volume = st.radio("Select Volume", list(volume_options.keys()))

# Button to make prediction
if st.button('Predict'):
    # Initialize the features dictionary
    input_features = {
        'county_number': [county_number],
        'week': [week],
    }
    
    # Add the volume features based on the selected volume
    for vol in volume_options.keys():
        input_features[vol] = [1 if selected_volume == vol else 0]
    
    # Add the alcohol type features
    for alcohol in alcohol_type_options.keys():
        input_features[alcohol] = [1 if selected_alcohol_type == alcohol else 0]
    
    # Add the bottle volume features
    for bottle_vol in bottle_volume_options.keys():
        input_features[bottle_vol] = [1 if bottle_volume == bottle_vol else 0]
    
    # Add the pack features
    for pack_key in pack_options.keys():
        input_features[pack_key] = [1 if pack == pack_key else 0]
    
    # Create the DataFrame
    input_df = pd.DataFrame(input_features)

    # Reorder the DataFrame columns to match the training data
    # This step assumes you know the order of the columns used in the model training
    correct_order = xgboost_model.get_booster().feature_names
    input_df = input_df[correct_order]

    # Display the input features for verification
    st.dataframe(input_df)
    st.write("------")

    # Make prediction
    prediction = xgboost_model.predict(input_df)
    st.write(f'Predicted Profits: ${prediction[0]:.2f}')

