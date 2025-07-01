# MQL Deal Analysis Dashboard

This project provides a comprehensive analysis of Marketing Qualified Leads (MQLs) through an interactive Streamlit dashboard. It processes raw sales data, transforms it into a usable format, and presents various analyses, including monthly deal flow, sales funnel conversion rates, and deal owner performance.

## Features

- **Data Transformation**: Automatically converts wide-format Excel data into a long-format CSV suitable for analysis.
- **Interactive Dashboard**: A Streamlit application to visualize and explore the MQL data.
- **Pipeline Overview**: Get a snapshot of the sales pipeline, including deal distribution and MRR by stage.
- **Time Series Analysis**: Track trends in deal volume and MRR over time.
- **Performance Metrics**: Analyze the performance of deal owners.
- **Funnel Analysis**: Visualize the conversion rates through different sales stages.
- **Network Accessibility**: Easily launch the dashboard to be accessible over your local network.

## Pipeline Logic

The data pipeline consists of two main steps:

1.  **Data Conversion**: The `excel_to_csv.py` script reads the source Excel file (`Dataset/New MQLs Dataset.xlsx`), which is in a wide format. It then transforms the data into a long format, where each row represents a specific event (entering or exiting a stage) for a deal. The output is saved as `Dataset/mql.csv`. This script is automatically run when you start the dashboard.

2.  **Dashboard Visualization**: The `streamlit_dashboard.py` script reads the generated `mql.csv` and creates the interactive dashboard.

## How to Run the Dashboard

You have two options for running the dashboard: locally on your machine or making it accessible to others on your network.

### 1. Running Locally

To run the dashboard and access it only on your computer, use the following command:

```bash
./run_dashboard.sh
```

This script will:
1.  Install the required Python packages from `requirements.txt`.
2.  Run the `excel_to_csv.py` script to perform the data transformation.
3.  Launch the Streamlit dashboard.

You can then access the dashboard at `http://localhost:8501`.

### 2. Running on a Network

To share the dashboard with others on the same Wi-Fi or local network, use the network-enabled launch script:

```bash
./start_network_dashboard.sh
```

This script will:
1.  Perform the same data transformation as the local script.
2.  Detect your computer's local IP address.
3.  Launch the Streamlit dashboard, making it accessible from other devices on your network.

After running the script, it will display the URL you can use to access the dashboard from other devices (e.g., `http://192.168.1.100:8501`).

### 3. Sharing Over the Internet (Advanced)

If you need to share the dashboard over the internet, you can use a tunneling service like `ngrok`.

1.  **Install ngrok**: Download and install it from [ngrok.com](https://ngrok.com/download).

2.  **Start the dashboard locally**:
    ```bash
    ./run_dashboard.sh
    ```

3.  **Create an ngrok tunnel**: In a new terminal window, run:
    ```bash
    ngrok http 8501
    ```

4.  **Share the URL**: `ngrok` will provide you with a public URL (e.g., `https://random-string.ngrok.io`) that you can share with anyone.

## Project Structure

```
.
├── Dataset/
│   ├── New MQLs Dataset.xlsx  # Source data
│   └── mql.csv                # Transformed data
├── excel_to_csv.py            # Data transformation script
├── streamlit_dashboard.py     # Main dashboard application
├── run_dashboard.sh           # Script to run the dashboard locally
├── start_network_dashboard.sh # Script to run the dashboard on a network
├── requirements.txt           # Python package dependencies
└── README.md                  # This file
```
