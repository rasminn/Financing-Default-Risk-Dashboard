import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your merged DataFrame
try:
    df = pd.read_csv('merged_dataset.csv')
except FileNotFoundError:
    st.error("Error: 'merged_dataset.csv' not found. Please make sure it's in the same directory.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("Error: 'merged_dataset.csv' is empty.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the dataset: {e}")
    st.stop()

st.title("📊 Financing Default Risk Dashboard")

# Summary
st.header("Overview")
st.metric("Total Customers", len(df))
st.metric("Default Rate", f"{df['is_default'].mean() * 100:.2f}%")

# Filters
st.sidebar.header("Filter Customers")
age = st.sidebar.slider("Age", int(df['age'].min()), int(df['age'].max()), (25, 45))
income = st.sidebar.slider("Monthly Income", 1000, 20000, (3000, 8000))

filtered_df = df[(df['age'].between(*age)) & (df['monthly_income'].between(*income))]
st.subheader(f"Filtered Data Size: {len(filtered_df)}")

# Default Rate by Employment Type
st.subheader("Default Rate by Employment Type")
fig_emp, ax_emp = plt.subplots()
sns.barplot(data=filtered_df, x='employment_type_description', y='is_default', estimator=lambda x: sum(x)/len(x), ax=ax_emp)
ax_emp.set_ylabel("Default Rate")
ax_emp.set_xlabel("Employment Type")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig_emp)
st.markdown("This chart illustrates the default rate across different employment types within the currently filtered customer segment. Observe the varying default risks associated with each category.")

# Distribution of DTI by Default Status
st.subheader("Distribution of DTI by Default Status")
fig_dti, ax_dti = plt.subplots()
sns.boxplot(data=filtered_df, x='is_default', y='DTI', ax=ax_dti)
ax_dti.set_xticks([0, 1])
ax_dti.set_xticklabels(['No Default (0)', 'Default (1)'])
ax_dti.set_ylabel("Debt-to-Income Ratio (DTI)")
ax_dti.set_xlabel("Default Status")
st.pyplot(fig_dti)
st.markdown("This box plot compares the distribution of the Debt-to-Income (DTI) ratio for customers who did and did not default. Analyze the central tendencies and spread of DTI for each group to understand its relationship with default.")

# Distribution of Repayment Ratio by Default Status
st.subheader("Distribution of Repayment Ratio by Default Status")
fig_repay, ax_repay = plt.subplots()
sns.boxplot(data=filtered_df, x='is_default', y='repayment_ratio', ax=ax_repay)
ax_repay.set_xticks([0, 1])
ax_repay.set_xticklabels(['No Default (0)', 'Default (1)'])
ax_repay.set_ylabel("Repayment Ratio")
ax_repay.set_xlabel("Default Status")
st.pyplot(fig_repay)
st.markdown("This chart shows the distribution of the repayment ratio based on default status. Compare the distributions to see if a customer's repayment history (relative to the loan term) differs between those who default and those who do not.")

# Confusion Matrix (Optional)
st.subheader("Confusion Matrix")
try:
    st.image("confusion_matrix.png")  # Save confusion matrix plot from your notebook
except FileNotFoundError:
    st.warning("Warning: 'confusion_matrix.png' not found. Please make sure it's in the same directory if you want to display it.")
st.markdown("This is the confusion matrix, showing the performance of our predictive model. It details the true positives, true negatives, false positives, and false negatives.")

# Recommendations
st.header("📌 Key Recommendations")
st.markdown("""
- **Flag customers with DTI > 0.6 and repayment ratio < 0.3:** This rule identifies customers with high debt relative to income and a poor repayment history, indicating higher risk.
- **Consider closer monitoring of private-sector employees:** The employment type analysis suggests a potentially higher default rate in this sector within the filtered data.
- **Implement strategies to better identify potential defaulters:** The confusion matrix (if visible) highlights areas where the current model could be improved to reduce false negatives.
- **Further analysis on the distributions of DTI and repayment ratio:** A deeper statistical look at these features could help refine the thresholds used for risk assessment.
""")