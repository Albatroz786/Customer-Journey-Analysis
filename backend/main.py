from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is working!"}

# Allow CORS for frontend-backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class CustomerData(BaseModel):
    data: list[dict]  # Expecting list of customer data rows as dictionaries

@app.post("/analyze/")
def analyze(data: CustomerData):
    df = pd.DataFrame(data.data)

    # Drop non-numeric ID column (optional)
    if "CustomerID" in df.columns:
        df = df.drop(columns=["CustomerID"])

    # One-hot encode categorical variables
    df_encoded = pd.get_dummies(df, columns=["ReferralSource", "DeviceType"])

    # Scale numerical + encoded features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_encoded)

    # Dimensionality reduction using PCA
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(scaled_data)

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(reduced_data)

    # Prepare the response
    response = {
        "reduced_data": reduced_data.tolist(),
        "clusters": clusters.tolist(),
        "explained_variance_ratio": pca.explained_variance_ratio_.tolist()
    }
    return response

# Run the app using: uvicorn backend.main:app --reload
