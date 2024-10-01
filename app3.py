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

# Section: Input Ingredients
st.header("Input Ingredients")

# Text area for listing ingredients
input_ingredients = st.text_area(
    "List the ingredients (separated by commas):"
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

    # Process ingredient allergies
    allergy_list = [
        allergy.strip().lower()
        for allergy in ingredient_allergies.split(",")
        if allergy.strip()
    ]

    # Process input ingredients
    ingredient_list = [
        ingredient.strip()
        for ingredient in input_ingredients.split(",")
        if ingredient.strip()
    ]

    # Section: Display Ingredients with Highlighted Allergens
    st.header("Ingredients Analysis")

    # CSS for tooltip functionality
    st.markdown(
        """
        <style>
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            margin-bottom: 5px;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 220px;
            background-color: #555;
            color: #fff;
            text-align: left;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%; /* Adjust as needed */
            left: 50%;
            margin-left: -110px; /* Adjust as needed */
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 12px;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }

        /* Arrow at the bottom of the tooltip */
        .tooltip .tooltiptext::after {
            content: "";
            position: absolute;
            top: 100%; /* At the bottom of the tooltip */
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: #555 transparent transparent transparent;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    for idx, ingredient in enumerate(ingredient_list):
        if idx == 0:
            # First ingredient: display in red with tooltip
            st.markdown(
                f"""
                <div class="tooltip">
                    <span style="color:red">{ingredient}</span>
                    <span class="tooltiptext">This ingredient was flagged because it is known to cause irritation.</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif ingredient.lower() in allergy_list:
            # Display allergen ingredients in red font
            st.markdown(
                f"<span style='color:red'>{ingredient}</span>",
                unsafe_allow_html=True,
            )
        else:
            st.write(ingredient)

    # Placeholder for processing all inputs and generating results
    # You can add your data handling and analysis code here
