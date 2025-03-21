import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit UI
st.title("Customer Journey Analysis")

uploaded_file = st.file_uploader("Upload Customer Data (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)

    if st.button("Analyze"):
        # Send data to backend
        response = requests.post(
            "http://127.0.0.1:8000/analyze/",
            json={"data": df.to_dict(orient="records")}
        )
        
        if response.status_code == 200:
            result = response.json()
            reduced_data = pd.DataFrame(result["reduced_data"], columns=["PCA1", "PCA2"])
            reduced_data["Cluster"] = result["clusters"]

            st.write("Clustering Result:")
            st.write(reduced_data)

            # Plot clusters
            plt.figure(figsize=(8, 6))
            sns.scatterplot(
                x="PCA1",
                y="PCA2",
                hue="Cluster",
                palette="viridis",
                data=reduced_data
            )
            st.pyplot(plt)
        else:
            st.error("Failed to analyze data!")

