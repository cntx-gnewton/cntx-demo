import streamlit as st

# Title of the application
st.title("Skin Profile Assessment")

# Section: Environmental Factors Questionnaire
st.header("Environmental Factors Questionnaire")

# Age input
age = st.number_input("What is your age?", min_value=0,
                      max_value=120, value=25)

# Gender selection
gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"])

# Sun exposure level
sun_exposure = st.selectbox(
    "How much sun exposure do you get daily?", ["Low", "Moderate", "High"]
)

# Pollution exposure level
pollution_exposure = st.selectbox(
    "How polluted is your environment?", ["Low", "Moderate", "High"]
)

# Stress level
stress_level = st.selectbox(
    "What is your current stress level?", ["Low", "Moderate", "High"]
)

# Section: Skin Conditions
st.header("Skin Conditions")

# Multiple selection for skin conditions
skin_conditions = st.multiselect(
    "Select any skin conditions you have:",
    [
        "Acne",
        "Eczema",
        "Rosacea",
        "Psoriasis",
        "Dermatitis",
        "Hyperpigmentation",
        "Other",
    ],
)

# Additional input if 'Other' is selected
if "Other" in skin_conditions:
    other_conditions = st.text_input("Please specify other skin conditions:")

# Section: Ingredient Allergies
st.header("Ingredient Allergies")

# Text area for listing ingredient allergies
ingredient_allergies = st.text_area(
    "List any ingredient allergies you have (separated by commas):"
)

# Section: Upload 23andMe Genome Data
st.header("Upload Your 23andMe Genome Data")

# File uploader for genome txt file
genome_file = st.file_uploader(
    "Upload your 23andMe genome txt file:", type=["txt"]
)

# Check if a file has been uploaded
if genome_file is not None:
    st.success("Genome file uploaded successfully!")
    # Placeholder for processing the genome file
    # genome_data = genome_file.getvalue()
    # Process the genome_data as needed

# Submit button
if st.button("Submit"):
    st.write("Processing your data...")
    # Placeholder for processing all inputs and generating results
    # You can add your data handling and analysis code here
