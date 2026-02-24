Customer Segment Profiles
Overview

Customer segmentation was performed using K-Means clustering (3 clusters) after feature scaling. Hierarchical clustering and DBSCAN were also applied for comparison. Final segmentation is based on K-Means results for business interpretation and model building.

Segment 0 – Loyal & Stable Customers
Characteristics:

Higher tenure

Lower churn rate

Consistent service usage

Stable behavioral patterns

Interpretation:

These customers are long-term users who show loyalty and consistent engagement with the service. Their probability of churn is relatively low.

Business Value:

High retention value and predictable revenue stream.

Segment 1 – At-Risk Customers
Characteristics:

Lower tenure

Higher churn rate

Possible dissatisfaction or low engagement

Higher volatility in usage patterns

Interpretation:

These customers are more likely to churn and require immediate retention strategies.

Business Risk:

Revenue loss if proactive measures are not taken.

Segment 2 – Growth Opportunity Customers
Characteristics:

Medium tenure

Moderate churn probability

Potential for upselling

Active but not fully engaged

Interpretation:

These customers are not fully loyal yet but show potential for long-term retention with the right incentives.

Business Opportunity:

High potential for cross-selling and premium upgrades.

Clustering Methodology

Data scaled using StandardScaler

K-Means applied with optimal cluster selection using Elbow Method

Hierarchical clustering and DBSCAN used for comparison

Final segmentation selected based on interpretability and cluster balance
