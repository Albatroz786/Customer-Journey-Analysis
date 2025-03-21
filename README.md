<h1><b>Customer Journey Analysis Using Clustering and Dimensionality Reduction</b></h1>
<h2>🚀Project Overview</h2>

<h4>This project analyzes customer journeys using Clustering and Dimensionality Reduction to identify customer behavior patterns and improve the user experience. The backend is built using FastAPI to handle clustering and data processing, while the frontend is built using Streamlit for visualization.

</h4>

<h2><b>🌟 Features</b></h2>

<h4>
  
* Customer Data Clustering – Uses KMeans clustering to identify customer groups.

* Dimensionality Reduction – Uses PCA (Principal Component Analysis) to reduce data dimensions for visualization.

* Data Visualization – Displays clusters using scatter plots.

* Real-time Analysis – Allows real-time cluster analysis through API.

* Interactive Frontend – Built with Streamlit for easy interaction and visualization.</h4><br>


<h2><b>📁 Project Structure</b></h2>

1. Clone the Repository

   * Open your terminal and clone the repository:

2. Navigate to the Project Folder

   * Move into the project folder:

3. Create a Virtual Environment

   * Create a virtual environment to isolate dependencies:

4. Activate Virtual Environment

   * Windows:

   * Linux/macOS:

5. Install Dependencies

   * Install all required dependencies:

6. Add Customer Data

   * Create a `data` folder in the root directory:

   * Add `customer_data.csv` with sample data:
  

<br>
<h2>Structure</h2>

```
<h2>customer-journey-analysis/
├── backend/
│   └── main.py
├── frontend/
│   ├── app.py
│   └── data.csv
├── venv/
└── requirements.txt</h2>

```
  

<br><h2><b>▶️ Running the Project</b></h2>

<h3>1. Start Backend</h3>

Navigate to the backend folder:

Start the FastAPI server:

✅ The backend will run at: http://127.0.0.1:8000

<h3><b>Backend Endpoints:</b></h3>

* `GET /` → Test if backend is working

* `GET /cluster` → Returns clustering graph

* `GET /get-cluster-data` → Returns cluster data in JSON format


<br><h3><b>2. Start Frontend</b></h3>

Open a new terminal and navigate to the frontend folder:

Start the Streamlit app:

✅ The frontend will run at: http://localhost:8501


<br><h3><b>3. Run in VS Code</b></h3>

1. Open VS Code

   * Open VS Code and navigate to the project folder.

2. Open Terminal in VS Code

   * Open the terminal in VS Code (View → Terminal).

3. Activate Virtual Environment

   * Windows:

   * Linux/macOS:

4. Run Backend in VS Code Terminal

   * Open a new terminal tab and navigate to the backend folder:

   * Start FastAPI:

5. Run Frontend in VS Code Terminal

   * Open a new terminal tab and navigate to the frontend folder:

   * Start Streamlit:

✅ The backend will run at `http://127.0.0.1:8000`<br>
✅ The frontend will run at `http://localhost:8501`


<br><h3><b>4. Test the Project</b></h3>

1. Open the backend Swagger UI:

2. Open the frontend in your browser:

✅ You should see:

* Cluster graph showing different clusters.

* Data table with customer cluster details.


<br><h2>🌐 API Endpoints</h2>


| Endpoint             | Method |  Description        |
|----------------------|--------|---------------------|
| `/`                  | GET    |  Check if backend is working |
| `/cluster`           | GET    |  Returns customer clustering graph |
| `/get-cluster-data`  | GET    |  Returns clustered customer data |

 
<br><h2><b>📊 PCA and Scatter Plot Details</b></h2>

1. Principal Component Analysis (PCA):

   * PCA reduces the dimensionality of customer data.

   * It identifies the most important features that explain variance in the data.

   * The first two principal components are plotted on the X-axis and Y-axis.

2. Scatter Plot Details:

   * Each point represents a customer projected onto the PCA space.

   * Different colors represent different clusters.

   * Centroids (marked with an 'X') represent the center of each cluster.

   * Similar customers (in terms of behavior) are grouped closer together.

   * Outliers or distinct customer behaviors appear farther from the cluster center.

3. Example Insight:

   * A cluster with high spending and engagement may form a distinct group.

   * A low-spending cluster with short session times may indicate disengaged users.
  

<br><h2><b>❗ Troubleshooting</b></h2>

1. Backend not starting – Ensure all dependencies are installed.

2. Streamlit not recognized – Add Python Scripts path to `PATH`:

3. Data file not found – Ensure `customer_data.csv` is in the `data` folder.


<br><h2><b>💡 Future Improvements</b></h2>

* Add more clustering algorithms.

* Use t-SNE for better high-dimensional visualization.

* Add user authentication for personalized analysis.<br>


<h2>SnapShots</h2>



<img src ="https://github.com/user-attachments/assets/90519a3c-2af5-400a-94b6-299447742abf" width="600">

<img src ="https://github.com/user-attachments/assets/cc12a707-dedb-4a76-8002-47e55df26fc3" width="600">

<img src = "https://github.com/user-attachments/assets/db0170fe-3789-4cde-b597-5f0755b5f2df" width="600">


































