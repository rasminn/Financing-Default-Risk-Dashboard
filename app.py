import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your merged DataFrame
try:
    df = pd.read_csv('merged_dataset_sample.csv')
except FileNotFoundError:
    st.error("Error: 'merged_dataset_sample.csv' not found. Please make sure it's in the same directory.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("Error: 'merged_dataset_sample.csv' is empty.")
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

#risk scoring
def compute_risk_score(row):
    score = 0
    if row['DTI'] > 0.6:
        score += 1
    if row['repayment_ratio'] < 0.3:
        score += 1
    if row['age'] < 30:
        score += 1
    if row['monthly_income'] < 5000:
        score += 1
    if 'Private' in row['employment_type_description']:
        score += 1
    return score

filtered_df['risk_score'] = filtered_df.apply(compute_risk_score, axis=1)

def risk_label(score):
    if score <= 1:
        return "Low Risk ✅"
    elif score <= 3:
        return "Medium Risk ⚠️"
    else:
        return "High Risk 🔥"

filtered_df['risk_category'] = filtered_df['risk_score'].apply(risk_label)
st.subheader("🧮 Customer Risk Scoring Table")
st.write("This table classifies each customer into Low, Medium, or High risk based on financial indicators:")

st.dataframe(filtered_df[['age', 'monthly_income', 'DTI', 'repayment_ratio', 'employment_type_description', 'risk_score', 'risk_category']].sort_values(by='risk_score', ascending=False).reset_index(drop=True))

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

# key insights
st.header("📌 Key Insights from the Dashboard")
st.markdown("""
- **Private sector employees** consistently show higher default rates compared to government or public-sector employees.
- Customers with **monthly income under RM5,000** show elevated default risk — particularly within private sector employment.
- **Younger customers (under age 30)** display a higher default rate, indicating greater financial volatility or less credit history.
- A specific **product type (likely Personal Financing)** dominates the default risk — suggesting the need for product-specific policy tightening.
- Combining low income, young age, and private sector employment highlights a **high-risk segment** worth closer scrutiny.
""")
