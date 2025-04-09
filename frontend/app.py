import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Apply custom dark-friendly CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #0e1117;
        color: #ffffff;
    }

    .main {
        background: #1e222a;
        padding: 3rem 2rem;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        max-width: 900px;
        margin: auto;
    }

    h1 {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        color: #e2e8f0;
        margin-bottom: 2rem;
    }

    .stFileUploader {
        border: 2px dashed #4a5568;
        background: #2d3748;
        border-radius: 12px;
        padding: 1.5rem;
    }

    .stButton>button {
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #2563eb, #06b6d4);
        transform: scale(1.03);
    }

    .css-1v3fvcr, .css-1d391kg {
        background-color: #2d3748;
        border-radius: 12px;
        padding: 10px;
    }

    .dataframe {
        background-color: #2d3748;
        color: #e2e8f0;
    }

    .plot-container {
        margin-top: 2rem;
        padding: 1rem;
        background-color: #1a202c;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("✨ Customer Journey Cluster Analyzer")

    uploaded_file = st.file_uploader("📁 Upload Customer Data (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Uploaded {len(df)} rows")

        st.subheader("📊 Data Preview")
        st.dataframe(df, height=300, use_container_width=True)

        if st.button("🚀 Analyze"):
            with st.spinner("Analyzing using PCA + KMeans..."):
                response = requests.post(
                    "http://127.0.0.1:8000/analyze/",
                    json={"data": df.to_dict(orient="records")}
                )

            if response.status_code == 200:
                result = response.json()
                reduced_data = pd.DataFrame(result["reduced_data"], columns=["PCA1", "PCA2"])
                reduced_data["Cluster"] = result["clusters"]

                st.success("🎉 Analysis Complete!")

                st.subheader("📌 Clustering Result")
                st.dataframe(reduced_data, height=300)

                # Download
                csv = reduced_data.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ Download Result", csv, "clustered_data.csv", "text/csv")

                # Plot
                st.subheader("📈 Cluster Visualization")
                with st.container():
                    plt.figure(figsize=(8, 6))
                    sns.set(style="darkgrid")
                    sns.scatterplot(
                        x="PCA1",
                        y="PCA2",
                        hue="Cluster",
                        palette="cool",
                        data=reduced_data,
                        s=100,
                        edgecolor="black"
                    )
                    plt.title("Customer Segments", fontsize=16)
                    plt.xlabel("Principal Component 1")
                    plt.ylabel("Principal Component 2")
                    st.pyplot(plt)
            else:
                st.error("❌ Analysis failed. Check backend or data formatting.")
    else:
        st.info("📂 Please upload a CSV file to get started.")

    st.markdown("</div>", unsafe_allow_html=True)


