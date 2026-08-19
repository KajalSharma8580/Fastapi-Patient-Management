import streamlit as st
import requests


# --------------------------------------------------
# FastAPI URL
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/predict"


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below:")


# --------------------------------------------------
# Input Fields
# --------------------------------------------------

age = st.number_input(
    "Age",
    min_value=1,
    max_value=119,
    value=30
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    value=65.0
)

height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=1.7
)

income_lpa = st.number_input(
    "Annual Income (LPA)",
    min_value=0.1,
    value=10.0
)

smoker = st.selectbox(
    "Are you a smoker?",
    options=[True, False]
)

city = st.text_input(
    "City",
    value="Mumbai"
)

occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]
)


# --------------------------------------------------
# Prediction Button
# --------------------------------------------------

if st.button("Predict Premium Category"):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:

        # ------------------------------------------
        # Send request to FastAPI
        # ------------------------------------------

        response = requests.post(
            API_URL,
            json=input_data,
            timeout=10
        )


        # ------------------------------------------
        # Successful Response
        # ------------------------------------------

        if response.status_code == 200:

            result = response.json()

            if "response" in result:

                prediction = result["response"]

                # Predicted Category
                st.success(
                    f"Predicted Insurance Premium Category: "
                    f"**{prediction['predicted_category']}**"
                )


                # Confidence
                if prediction.get("confidence") is not None:

                    confidence = prediction["confidence"]

                    st.write(
                        "🔍 Confidence:",
                        f"{confidence:.2%}"
                    )


                # Class Probabilities
                if prediction.get("class_probabilities") is not None:

                    st.write("📊 Class Probabilities:")

                    st.json(
                        prediction["class_probabilities"]
                    )

            else:

                st.error(
                    "❌ Unexpected response format from FastAPI."
                )

                st.json(result)


        # ------------------------------------------
        # FastAPI Error
        # ------------------------------------------

        else:

            st.error(
                f"❌ FastAPI Error: {response.status_code}"
            )

            try:

                error_data = response.json()

                st.json(error_data)

            except requests.exceptions.JSONDecodeError:

                st.write(
                    "Server Response:",
                    response.text
                )


    # ----------------------------------------------
    # Connection Error
    # ----------------------------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to FastAPI server."
        )

        st.info(
            "Make sure FastAPI is running on "
            "http://127.0.0.1:8000"
        )


    # ----------------------------------------------
    # Timeout Error
    # ----------------------------------------------

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ FastAPI server took too long to respond."
        )


    # ----------------------------------------------
    # Other Request Errors
    # ----------------------------------------------

    except requests.exceptions.RequestException as e:

        st.error(
            f"❌ Request failed: {e}"
        )