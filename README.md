# Loan Default Risk Dashboard

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
-   **Key Metrics:** Displays the total number of customers and the overall default rate.
-   **Employment Type Analysis:** Bar chart showing the default rate for different employment categories within the filtered data.
-   **Feature Distributions:** Box plots illustrating the distribution of DTI and Repayment Ratio, separated by default status.
-   **Confusion Matrix (Optional):** If `confusion_matrix.png` is present, it will display the performance of a predictive model.
-   **Key Recommendations:** Actionable insights based on the visualized data.

## Repository Contents

-   `app.py`: The main Streamlit application code.
-   `merged_dataset.csv`: The merged dataset used for analysis (you'll need to generate this from your data).
-   `requirements.txt`: Lists the Python libraries required to run the app.
-   `confusion_matrix.png` (Optional): An image of the confusion matrix from your model evaluation.
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

3.  **Ensure your merged dataset `merged_dataset.csv` is in the same directory.**

## Running the App

To run the Streamlit dashboard, navigate to the repository directory in your terminal and execute:

```bash
streamlit run app.py
