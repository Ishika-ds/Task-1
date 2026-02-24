# Customer Segmentation Profiles

## Project Overview

Customer segmentation was performed using clustering algorithms to group customers based on behavioral patterns. The primary algorithm used for final segmentation was K-Means clustering, with Hierarchical Clustering and DBSCAN applied for comparison.

The objective was to create meaningful customer groups and support segment-specific predictive modeling.

---

## Segmentation Methodology

- Data preprocessing included handling missing values and encoding categorical variables.
- Features were standardized using StandardScaler.
- The optimal number of clusters was determined using the Elbow Method.
- K-Means clustering was applied with 3 clusters.
- Hierarchical Clustering and DBSCAN were used for comparative analysis.

---

## Segment 0 – Loyal & Stable Customers

### Key Characteristics

- Higher customer tenure
- Lower churn probability
- Consistent service usage
- Stable behavioral patterns

### Business Interpretation

These customers demonstrate loyalty and long-term engagement. They contribute to steady revenue and have a lower likelihood of churn.

### Business Value

- High customer lifetime value
- Strong retention stability
- Potential brand advocates

---

## Segment 1 – At-Risk Customers

### Key Characteristics

- Lower tenure
- Higher churn rate
- Lower engagement levels
- Unstable usage patterns

### Business Interpretation

This segment represents customers who are more likely to churn. Immediate intervention strategies are necessary to reduce potential revenue loss.

### Business Risk

- Increased churn probability
- Revenue leakage if not addressed

---

## Segment 2 – Growth Opportunity Customers

### Key Characteristics

- Medium tenure
- Moderate churn probability
- Active but not fully loyal
- Upselling potential

### Business Interpretation

These customers show potential for long-term retention with proper engagement strategies. They are ideal candidates for marketing campaigns and premium upgrades.

### Business Opportunity

- Cross-selling opportunities
- Conversion to higher-value plans
- Increased engagement potential

---

## Summary

The segmentation process successfully divided customers into three meaningful groups:

1. Loyal & Stable Customers
2. At-Risk Customers
3. Growth Opportunity Customers

These segments enable targeted business strategies, improve predictive modeling accuracy, and support data-driven decision-making.
