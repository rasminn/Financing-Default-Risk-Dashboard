# Loan Default Risk Dashboard

**Disclaimer:** Please note that this dashboard is currently using a subset of the full `merged_dataset.csv` due to file size limitations for this deployment. The full analysis was conducted on a larger dataset.

This Streamlit application visualizes factors contributing to loan default using a merged customer and financial dataset. The dashboard allows users to explore potential risk indicators through interactive filters and charts.

## Overview

The dashboard provides insights into:

-   Overall default rate of customers.
-   Default rates based on employment type within filtered segments.
-   Distribution of Debt-to-Income (DTI) ratio for defaulting and non-defaulting customers.
-   Distribution of the Repayment Ratio for defaulting and non-defaulting customers.
-   (Optional) Visualization of the model's performance via a confusion matrix.

## Features

-   **Interactive Filters:** Adjust the displayed data by age and monthly income using sidebar sliders.
-   **Key Metrics:** Displays the total number of customers and the overall default rate (based on the subset).
-   **Employment Type Analysis:** Bar chart showing the default rate for different employment categories within the filtered data (based on the subset).
-   **Feature Distributions:** Box plots illustrating the distribution of DTI and Repayment Ratio, separated by default status (based on the subset).
-   **Confusion Matrix (Optional):** If `confusion_matrix.png` is present, it will display the performance of a predictive model trained on the full dataset.
-   **Key Recommendations:** Actionable insights based on the analyzed data.

## Repository Contents

-   `app.py`: The main Streamlit application code.
-   `merged_dataset_sample.csv`: A sample of the merged dataset used for this deployed dashboard.
-   `requirements.txt`: Lists the Python libraries required to run the app.
-   `confusion_matrix.png` (Optional): An image of the confusion matrix from your model evaluation (likely trained on the full dataset).
-   `README.md`: This file.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd [repository name]
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ensure the sample dataset `merged_dataset_sample.csv` is in the same directory.**

## Running the App

To run the Streamlit dashboard, navigate to the repository directory in your terminal and execute:

```bash
streamlit run app.py
